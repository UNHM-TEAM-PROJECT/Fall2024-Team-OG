import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
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

    return text

# Example usage - replace 'your_pdf.pdf' with the actual name of your PDF file
pdf_path = '2024-fall-comp690-M2-M3-jin.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
