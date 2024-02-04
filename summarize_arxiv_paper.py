import os

from utils.pdf_helper.read_pdf_from_local import read_pdf_exclude_pages
from utils.pdf_helper.get_pdf_from_arxiv import read_pdf_from_url
from utils.pdf_helper.pdf_summary_report_writer import create_or_append_pdf
from utils.transformers.openai_summarizer import openAI_summarizer_wrapper


def summarize_local_pdf_using_openai(input_file, output_file, pages_to_exclude):
    input_file_content = read_pdf_exclude_pages(input_file, pages_to_exclude)
    summarized_report = openAI_summarizer_wrapper(input_file_content)
    print(summarized_report)
    create_or_append_pdf(output_file, summarized_report)
    return


base_input_path = "paper_pdf_repo/research_papers/"
base_output_path = "paper_pdf_repo/summaries/"
input_filename = (
    "SLICEGPT_COMPRESS_LARGE_LANGUAGE_MODELS_BY_DELETING_ROWS_AND_COLUMNS.pdf"
)
output_filename = (
    "SLICEGPT_COMPRESS_LARGE_LANGUAGE_MODELS_BY_DELETING_ROWS_AND_COLUMNS_Summary.pdf"
)
input_file = os.path.join(base_input_path, input_filename)
output_file = os.path.join(base_output_path, output_filename)
pages_to_exclude = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]


summarize_local_pdf_using_openai(input_file, output_file, pages_to_exclude)