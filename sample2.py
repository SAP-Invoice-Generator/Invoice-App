import fitz  # PyMuPDF
import easyocr
import re
import os

def extract_invoice_info(pdf_path):
    invoice_info = {}

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Loop through each page of the PDF
    for page_num in range(len(doc)):
        # Get the page
        page = doc.load_page(page_num)
        
        # Render the page as an image
        pix = page.get_pixmap()
        image_path = f"page_{page_num}.png"
        pix.save(image_path)
        
        # Perform OCR on the image
        result = reader.readtext(image_path)

        # Extracted text
        extracted_text = ' '.join([entry[1] for entry in result])

        # Extract invoice number
        match_invoice_number = re.search(r'Invoice\s*Number:\s*(\w+)', extracted_text, re.IGNORECASE)
        if match_invoice_number:
            invoice_info['Invoice Number'] = match_invoice_number.group(1)

        # Extract billing name
        match_billing_name = re.search(r'Bill\s*To:\s*(.*?)Ship\s*To:', extracted_text, re.IGNORECASE | re.DOTALL)
        if match_billing_name:
            invoice_info['Billing Name'] = match_billing_name.group(1).strip()

        # Extract invoice date
        match_invoice_date = re.search(r'Invoice\s*Date:\s*(\d{2}/\d{2}/\d{4})', extracted_text, re.IGNORECASE)
        if match_invoice_date:
            invoice_info['Invoice Date'] = match_invoice_date.group(1)

        # Extract due date
        match_due_date = re.search(r'Due\s*Date:\s*(\d{2}/\d{2}/\d{4})', extracted_text, re.IGNORECASE)
        if match_due_date:
            invoice_info['Due Date'] = match_due_date.group(1)

        # Extract total amount
        match_total_amount = re.search(r'Total\s*Amount:\s*\$?(\d+\.\d{2})', extracted_text, re.IGNORECASE)
        if match_total_amount:
            invoice_info['Total Amount'] = match_total_amount.group(1)

        # Extract list of items
        match_items = re.search(r'Item\s*Quantity\s*Rate\s*Amount(.+?)Subtotal', extracted_text, re.IGNORECASE | re.DOTALL)
        if match_items:
            items_text = match_items.group(1).strip()
            items = []
            lines = items_text.split('\n')
            for i in range(0, len(lines), 4):
                quantity = lines[i].strip()
                description = lines[i+1].strip()
                unit_price = lines[i+2].strip()
                total_amount = lines[i+3].strip()
                items.append({
                    'Quantity': quantity,
                    'Description': description,
                    'Unit Price': unit_price,
                    'Total Amount': total_amount
                })
            invoice_info['Items'] = items
        
        # Remove the temporary image file
        os.remove(image_path)

    # Close the PDF
    doc.close()

    return invoice_info

# Usage example
pdf_path = 'invoice/invoice_Aaron Bergman_36258.pdf'
invoice_info = extract_invoice_info(pdf_path)
print(invoice_info)
