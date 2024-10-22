# arXiv Research Paper (PDF) Summarization Tool
This repository houses a Python tool designed to process and summarize arXiv research papers (PDF files), making them more accessible and easier to digest.
This tool creates a summarized report (a PDF file) of the research making the original research paper easier to read and more accessible.
 *This tool is intended for education and informational purposes only and original IP remains with the author of the research paper.* 

## Features

- **PDF Reader**: Reads PDF files, with the option to exclude specific pages as provided by the user (references and some other pages towards the end of the report).
- **OpenAI Summarizer**: A Summarizes the research paper by creating smaller chunks and then summarizing each chunk and then consolidating all the part summaries to create a final overall summary. The tool uses OpenAI's GPT 4 model and requires a paid OpenAI API key.
- **PDF Writer**: Creates or appends Summarized report to a PDF files specified by the user.

## How to use - Input and output file set up
- **Setting up input file**: default input pdf file path/directory is paper_pdf_repo/research_papers. Save the file in that dir. 
- **Setting up output file**: default output folder where pdf file with summarized report is created is paper_pdf_repo/summaries
- **Setting up OpenAI API**: Rename the .env-example file to .env file and update it with your OpenAI API key.
- **Install required libraries**: use pip install -r requirements.txt to install required python packages to run the program.
- **Before Using**: update the input file name, output file name, and pages to exclude (generally last few pages with references etc.) in summarize_arxiv_paper.py (Will add this to streamlit UI in future). 
- **How to run**: After setting up API key, updating the pages to be excludes, and adjusting file name, execute summarize_arxiv_paper.py to run the tool.


## Upcoming Features
- **Open Source Model Summarizer**: Create the workflow using open source model to summarize research papers free of cost.
- **User Interface**: Create a streamlit user interface.
- **process pdf from arxiv URL**: No need to download the pdf file, user can just provide the url to the pdf file.
