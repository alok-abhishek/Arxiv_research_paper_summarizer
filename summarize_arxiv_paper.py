import os

from utils.pdf_helper.read_pdf_from_local import read_pdf_exclude_pages
from utils.pdf_helper.get_pdf_from_arxiv import read_pdf_from_url
from utils.pdf_helper.pdf_summary_report_writer import create_or_append_pdf
from utils.transformers.openai_summarizer import openAI_summarizer_wrapper
from utils.markdown.markdown_summary_report_writer import save_markdown_to_file


def summarize_local_pdf_to_pdf_using_openai(input_file, output_file, pages_to_exclude):
    input_file_content = read_pdf_exclude_pages(input_file, pages_to_exclude)
    summarized_report = openAI_summarizer_wrapper(input_file_content)
    create_or_append_pdf(output_file, summarized_report)
    return


def summarize_local_pdf_to_md_using_openai(input_file, output_file, pages_to_exclude):
    input_file_content = read_pdf_exclude_pages(input_file, pages_to_exclude)
    summarized_report = openAI_summarizer_wrapper(input_file_content)
    save_markdown_to_file(summarized_report, output_file)
    return


base_input_path = "paper_pdf_repo/research_papers/"
base_pdf_output_path = "paper_pdf_repo/summaries/"
base_md_output_path = "paper_md_repo/summaries/"
input_filename = "BBQ_A_Hand_Built_Bias_Benchmark_for_Question_Answering.pdf"
output_pdf_filename = (
    "BBQ_A_Hand_Built_Bias_Benchmark_for_Question_Answering_Summary.pdf"
)
output_md_filename = "BBQ_A_Hand_Built_Bias_Benchmark_for_Question_Answering_Summary.md"
input_file = os.path.join(base_input_path, input_filename)
output_pdf_file = os.path.join(base_pdf_output_path, output_pdf_filename)
output_md_file = os.path.join(base_md_output_path, output_md_filename)

pages_to_exclude = []

summarize_local_pdf_to_pdf_using_openai(input_file, output_pdf_file, pages_to_exclude)

summarize_local_pdf_to_md_using_openai(input_file, output_md_file, pages_to_exclude)
