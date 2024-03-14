import fitz  # PyMuPDF

def extract_raw_text(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Initialize variable to store raw text
    raw_text = ""
    
    # Loop through each page of the PDF
    for page in doc:
        # Extract text from the page
        text = page.get_text()
        
        # Append the extracted text to the raw text
        raw_text += text
    
    # Close the PDF
    doc.close()
    
    # Return the raw text
    return raw_text

# Example usage
pdf_path = 'invoice/invoice_Aaron Bergman_36258.pdf'  # Make sure the PDF file path is correct
raw_text = extract_raw_text(pdf_path)
print(raw_text)
