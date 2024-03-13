import tiktoken
from openai import OpenAI
import requests
import json
import dotenv
import os
import re


dotenv.load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


prompt_augmentation_file = "utils/transformers/prompt_instructions.json"
with open(prompt_augmentation_file, "r") as file:
    prompt_augmentation = json.load(file)

prompt_instruction = prompt_augmentation["openai_base_prompt_inst"]
openai_final_summary_prompt_inst = prompt_augmentation[
    "openai_final_summary_prompt_inst"
]

MAX_TOKEN_FOR_CONTEXT_WINDOW = 1000  # keeping it well short of 128,000 tokens context window of gpt-4-0125-preview to summarize in smaller chunks and not lose too much information.
TOKEN_FOR_CONTEXT_OVERLAP = (
    200  # overlap of 20% to not lose information in between two chunks
)


def count_tokens(input_string):
    encoding = tiktoken.get_encoding("cl100k_base")
    # from https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    num_tokens = len(encoding.encode(input_string))
    return num_tokens


def format_response(api_response):
    formatted_response = api_response.replace("\\n", "\n")
    formatted_response = re.sub(r"###\s*", "", formatted_response)
    formatted_response = re.sub(r"\*\*", "", formatted_response)
    formatted_response = re.sub(r"-\s\*\*", "", formatted_response)
    return formatted_response


def openAIsummarizer(text):
    try:
        openai_response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": prompt_instruction,
                },
                {"role": "user", "content": text},
            ],
            temperature=0.75,
        )
        summarized_text = openai_response.choices[0].message.content
        summarized_response = summarized_text + "\n"
        return summarized_response
    except Exception as e:
        print("Error during API call:", e)
        return "An error occurred while generating insights."


def openAI_final_summarizer(fragment_summaries):
    try:
        openai_response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": openai_final_summary_prompt_inst,
                },
                {"role": "user", "content": fragment_summaries},
            ],
            temperature=0.75,
        )
        summarized_text = openai_response.choices[0].message.content
        summarized_response = summarized_text + "\n"
        return summarized_response
    except Exception as e:
        print("Error during API call:", e)
        return "An error occurred while generating insights."


def openAI_summarizer_wrapper(text):
    token_count = count_tokens(text)
    if token_count <= MAX_TOKEN_FOR_CONTEXT_WINDOW:
        return openAIsummarizer(text)
    else:
        # Divide the text into chunks with TOKEN_FOR_CONTEXT_OVERLAP token overlap
        chunks = []
        start = 0
        while start < token_count:
            end = min(start + MAX_TOKEN_FOR_CONTEXT_WINDOW, token_count)
            if end < token_count:
                # Move the end back to ensure overlap
                overlap_start = end - TOKEN_FOR_CONTEXT_OVERLAP
                chunk_start = text.rfind(".", 0, overlap_start) + 1
                chunk_end = text.find(".", end) + 1
                if (
                    chunk_end == 0
                ):  # if no period is found, fall back to the end of the text
                    chunk_end = token_count
                chunk = text[chunk_start:chunk_end].strip()
            else:
                chunk = text[start:].strip()
            chunks.append(chunk)
            start = (
                chunk_end if end < token_count else token_count
            )  # Start next chunk after current chunk ends
        # Summarize each chunk and concatenate responses
        summarized_text = ""
        for chunk in chunks:
            summarized_response = openAIsummarizer(chunk)
            summarized_text += summarized_response + "\n"

        final_summary = openAI_final_summarizer(summarized_text)
        # final_summary_plus_chunk_summary = final_summary + summarized_text

        return final_summary
