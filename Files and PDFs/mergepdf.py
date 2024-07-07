import os
from PyPDF2 import PdfMerger

def merge_pdfs():
    # Get list of PDF files in current directory
    pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]
    pdf_files.sort()  # Sort PDF files in ascending order
    
    # Initialize PdfFileMerger object
    merger = PdfMerger()
    
    # Append each PDF to the merger object
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    
    # Write the merged PDF to a file
    with open('merged_pdf.pdf', 'wb') as output_file:
        merger.write(output_file)
    
    print("PDFs merged successfully!")

if __name__ == "__main__":
    merge_pdfs()
