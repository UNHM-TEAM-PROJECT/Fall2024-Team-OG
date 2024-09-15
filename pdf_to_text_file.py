import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt_path):
    # Open the PDF file
    document = fitz.open(pdf_path)

    # Initialize a variable to accumulate the extracted text
    text = ""

    # Iterate over each page in the document
    for page_number in range(document.page_count):
        # Select the page
        page = document[page_number]
        # Extract text from the page
        text += page.get_text()

    # Close the document
    document.close()

    # Write the extracted text to a text file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

    return text

# Example usage 
pdf_path = '2024-fall-comp690-M2-M3-jin.pdf'  # Your PDF file path
output_txt_path = 'extracted_text.txt'  #  Name of the output text file 
extracted_text = extract_text_from_pdf(pdf_path, output_txt_path)
print(extracted_text)  #  This will still print the text to the console
