import os
import textwrap
import re
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.enums import TA_JUSTIFY


def markdown_to_html(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"### (.*?)\n", r"<h3>\1</h3><br/>", text)
    text = re.sub(r"## (.*?)\n", r"<h2>\1</h2><br/>", text)
    text = re.sub(r"# (.*?)\n", r"<h1>\1</h1><br/>", text)
    return text


def create_or_append_pdf(output_file, text):
    text = markdown_to_html(text)  # Convert Markdown-style to HTML-style
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        "CustomStyle",
        parent=styles["Normal"],
        wordWrap="CJK",  # Better word wrapping
        allowWidows=1,
        allowOrphans=1,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
    )

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = [Spacer(1, 0.2 * inch), Paragraph(text, custom_style)]
    doc.build(story)

    if os.path.exists(output_file):
        existing_pdf = PdfReader(output_file)
        new_pdf = PdfReader(buffer)
        output = PdfWriter()

        for page in existing_pdf.pages:
            output.add_page(page)

        for page in new_pdf.pages:
            output.add_page(page)

        with open(output_file, "wb") as outputStream:
            output.write(outputStream)
    else:
        with open(output_file, "wb") as outputStream:
            outputStream.write(buffer.getvalue())


"""
base_output_path = "../../paper_pdf_repo/summaries/"
output_filename = "testing_output_Summary.pdf"
output_file = os.path.join(base_output_path, output_filename)
text_to_write = "Large language models have become the cornerstone of natural language process-ing, but their use comes with substantial costs in terms of compute and memory resources. Sparsification provides a solution to alleviate these resource constraints, and recent works have shown that trained models can be sparsified post-hoc. Existing sparsification techniques face challenges as they need additional data structures and offer constrained speedup with current hardware. In this paper we present SliceGPT, a new post-training sparsification scheme which replaces each weight matrix with a smaller (dense) matrix, reducing the embedding dimension of the network. Through extensive experimentation, we show that SliceGPT can remove up to 25% of the model parameters (including embeddings) for LLAMA -270B, OPT 66B and Phi-2 models while maintaining 99%, 99% and 90% zero-shot task performance of the dense model respectively. Our sliced models run on fewer GPUs and run faster without any additional code optimization: on 24GB consumer GPUs we reduce the total compute for inference on LLAMA -270B to 64% of that of the dense model; on 40GB A100 GPUs we reduce it to 66%. We offer a new insight, computational invariance in transformer networks, which enables SliceGPT and we hope it will inspire and enable future avenues to reduce memory and computation demands for pre-trained models. Code is available at: https://github.com/microsoft/TransformerCompression "
create_or_append_pdf(output_file, text_to_write)
"""
