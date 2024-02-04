import PyPDF2
import os


def is_pdf_file(filepath):
    return filepath.endswith(".pdf")


def read_pdf_exclude_pages(filepath, exclude_pages=[]):
    if not is_pdf_file(filepath):
        return "Error: Not a PDF file."

    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        content = ""
        for i in range(len(reader.pages)):
            if i not in exclude_pages:
                page = reader.pages[i]
                page_text = page.extract_text()
                if page_text:  # Check if text extraction is successful
                    content += page_text + "\n"
                    # print("page #:", i)
                else:
                    content += f"Unable to extract text from page {i + 1}\n"
    return content


"""
base_input_path = "../../paper_pdf_repo/research_papers/"
input_filename = (
    "SLICEGPT_COMPRESS_LARGE_LANGUAGE_MODELS_BY_DELETING_ROWS_AND_COLUMNS.pdf"
)
input_file = os.path.join(base_input_path, input_filename)
pages_to_exclude = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(read_pdf_exclude_pages(input_file, pages_to_exclude))
"""
