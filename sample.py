import re
from pdfminer.high_level import extract_text,extract_pages

# for pageLayout in extract_pages("1000+ PDF_Invoice_Folder\invoice_Aaron Bergman_36258.pdf"):
#     for element in pageLayout:
#         print(element)

text = extract_text("1000+ PDF_Invoice_Folder\invoice_Aaron Bergman_36258.pdf")
print(text) 