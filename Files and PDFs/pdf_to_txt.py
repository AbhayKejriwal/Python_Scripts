from PyPDF2 import PdfReader
import os

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

            # Get the directory path of the original PDF
            pdf_directory = os.path.dirname(pdf_file_path)

            # Construct the full path for the text file in the same directory
            txt_file_path = os.path.join(pdf_directory, txt_file_path)

            # Save the extracted text to the text file
            with open(txt_file_path, 'w', encoding='utf-8') as file:
                file.write(extracted_text)

            return txt_file_path
        else:
            return f"Failed to extract text from {pdf_file_path}"
    except Exception as e:
        return str(e)

def process_directory(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_file_path = os.path.join(root, file)
                result = process_pdf(pdf_file_path)
                print(result)
        for dir in dirs:
            subdirectory_path = os.path.join(root, dir)
            process_directory(subdirectory_path)  # Recursive call to process subdirectories

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to the folder containing PDF files
    folder_path = ''
    process_directory(folder_path)
