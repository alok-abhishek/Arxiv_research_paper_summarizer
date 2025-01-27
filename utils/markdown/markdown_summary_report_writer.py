import os
import logging


def save_markdown_to_file(markdown_content: str, output_file_path: str):
    """
    Saves a markdown-formatted string to a specified file path.

    Args:
        markdown_content (str): The markdown content to be saved.
        output_file_path (str): The full path of the output markdown file.

    Raises:
        ValueError: If the markdown_content is empty or the output_file_path is invalid.
        IOError: If there are issues writing to the file.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Validate inputs
    if not markdown_content:
        raise ValueError("Markdown content cannot be empty.")

    if not isinstance(output_file_path, str) or not output_file_path.strip():
        raise ValueError("Invalid output file path.")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file_path)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            logging.info(f"Created directories for path: {output_dir}")
        except Exception as e:
            logging.error(f"Failed to create directories for path {output_dir}: {e}")
            raise IOError(f"Could not create directories for path: {output_dir}")

    # Write the markdown content to the file
    try:
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(markdown_content)
            logging.info(f"Markdown content successfully saved to {output_file_path}")
    except Exception as e:
        logging.error(f"Failed to write to file {output_file_path}: {e}")
        raise IOError(f"Could not write to file: {output_file_path}")
