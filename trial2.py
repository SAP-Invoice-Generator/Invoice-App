import fitz  # PyMuPDF
import re

def extract_invoice_info(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Initialize variables to store invoice information
    invoice_number = None
    billing_name = None
    invoice_date = None
    due_date = None
    total_amount = None
    items = []

    # Loop through each page of the PDF
    for page in doc:
        # Extract text from the page
        text = page.get_text()
        print("Extracted text from page:")
        print(text)
        
        # Check for invoice number using regex
        if not invoice_number:
            match = re.search(r'Invoice\s*Number:\s*(\w+)', text, re.IGNORECASE)
            if match:
                invoice_number = match.group(1)
                print("Invoice Number:", invoice_number)
        
        # Check for billing name using regex
        if not billing_name:
            match = re.search(r'Billing\s*Name:\s*(.*)', text, re.IGNORECASE)
            if match:
                billing_name = match.group(1)
                print("Billing Name:", billing_name)
        
        # Check for invoice date using regex
        if not invoice_date:
            match = re.search(r'Invoice\s*Date:\s*(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
            if match:
                invoice_date = match.group(1)
                print("Invoice Date:", invoice_date)
        
        # Check for due date using regex
        if not due_date:
            match = re.search(r'Due\s*Date:\s*(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
            if match:
                due_date = match.group(1)
                print("Due Date:", due_date)
        
        # Check for total amount using regex
        if not total_amount:
            match = re.search(r'Total\s*Amount:\s*\$?(\d+\.\d{2})', text, re.IGNORECASE)
            if match:
                total_amount = match.group(1)
                print("Total Amount:", total_amount)
        
        # Check for items using regex
        item_matches = re.finditer(r'(\d+)\s+(.+?)\s+\$?(\d+\.\d{2})', text)
        for match in item_matches:
            items.append({
                'quantity': match.group(1),
                'description': match.group(2),
                'price': match.group(3)
            })
            print("Item:", match.group(1), match.group(2), match.group(3))
    
    # Close the PDF
    doc.close()
    
    # Return extracted information
    return {
        'invoice_number': invoice_number,
        'billing_name': billing_name,
        'invoice_date': invoice_date,
        'due_date': due_date,
        'total_amount': total_amount,
        'items': items
    }

# Example usage
pdf_path = 'invoice/invoice_Aaron Bergman_36258.pdf'  # Make sure the PDF file path is correct
invoice_info = extract_invoice_info(pdf_path)
