import PyPDF2
from io import BytesIO
import requests


def read_pdf_from_url(url, exclude_pages=[]):
    response = requests.get(url)
    if response.status_code == 200:
        reader = PyPDF2.PdfFileReader(BytesIO(response.content))
        content = ""
        for i in range(reader.numPages):
            if i not in exclude_pages:
                page = reader.getPage(i)
                content += page.extractText() + "\n"
        return content
    else:
        return "Error fetching the PDF file."


"""
pdf_url = "https://browse.arxiv.org/pdf/1706.03762.pdf"
exclude_pages = []  # page numbers to exclude
print(read_pdf_from_url(pdf_url, exclude_pages))
"""
