from PyPDF2 import PdfReader
import os
from file_operations import save_text_to_file

def extract_text_from_pdf(pdf_file_path):
    try:
        # Create a PdfReader object
        pdf_reader = PdfReader(pdf_file_path)

        # Initialize an empty string to store the extracted text
        text = ''

        # Loop through each page in the PDF
        for page in pdf_reader.pages:
            text += page.extract_text()

        return text
    except Exception as e:
        return str(e)

def process_pdf(pdf_file_path):
    try:
        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(pdf_file_path)

        if extracted_text:
            # Create a new file name with the same name as the PDF but with a .txt extension
            base_name = os.path.basename(pdf_file_path)
            txt_file_path = os.path.splitext(base_name)[0] + '.txt'

            # Save the extracted text to the text file using the save_text_to_file function
            saved_file_path = save_text_to_file(extracted_text, txt_file_path)

            return saved_file_path
        else:
            return "Failed to extract text from the PDF."
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_file_path = 'C:\\Users\\LENOVO\\Downloads\\Ethical Hacking Transcripts\\lec1.pdf'
    result = process_pdf(pdf_file_path)

    print(result)
