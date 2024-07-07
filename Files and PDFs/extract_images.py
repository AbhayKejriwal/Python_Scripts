import os
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)

        # Iterate through each image on the page
        for image_index, img in enumerate(image_list):
            # Get the XREF of the image
            xref = img[0]

            # Extract the image
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            # Save the image
            image_path = os.path.join(output_folder, f"page{page_num + 1}_image{image_index + 1}.png")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

    # Close the PDF
    pdf_document.close()

# Get the PDF file in the current folder
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]
if len(pdf_files) == 1:
    pdf_path = pdf_files[0]
    output_folder = os.getcwd()
    extract_images_from_pdf(pdf_path, output_folder)
else:
    print("Error: There should be exactly one PDF file in the current folder.")
