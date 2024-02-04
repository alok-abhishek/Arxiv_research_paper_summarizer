# arXiv Research Paper (PDF) Summarization Tool

This repository contains a Python code for processing arXiv Research Papers (PDF files) and create a summarize report (PDF) of the research.
This is to make the research paper easier to read and more accessible.  

## Features

- **PDF Reader**: Reads PDF files, with the option to exclude specific pages as provided by the user (references and some other pages towards the end of the report).
- **OpenAI Summarizer**: A Summarizes the research paper by creating smaller chunks and then summarizing each chunk and then consolidating all the part summaries to create a final overall summary. The tool uses OpenAI's GPT 4 model and requires a paid OpenAI API key.
- **PDF Writer**: Creates or appends Summarized report to a PDF files specified by the user.


## Features
- **Open Source Model Summarizer**: Create the workflow using open source model to summarize research papers free of cost.
- **User Interface**: Create a streamlit user interface.
- **process pdf from arxiv URL**: No need to download the pdf file, user can just provide the url to the pdf file.

## How to use - Input and output file set up
- **Open Source Model Summarizer**: default input pdf directory is paper_pdf_repo/research_papers 
- **Open Source Model Summarizer**: default output folder where pdf file with summarized report is created is paper_pdf_repo/summaries
- **To use**: update the input file name, output file name, and pages to exclude in summarize_arxiv_paper.py (Will add this to streamlit UI in future)
