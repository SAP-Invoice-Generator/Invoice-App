import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from .env file
load_dotenv()

# Get Supabase URL and Key from environment variables
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Create Supabase client
client = create_client(supabase_url, supabase_key)

# Create Invoices table
invoices_table = client.table("Invoices")
invoices_table.create({
    "invoice_id": "SERIAL PRIMARY KEY",  # Assuming SERIAL is used for auto-incrementing IDs
    "employee_id": "INT REFERENCES User_Companies(employee_id)",
    "employer_id": "INT REFERENCES Employers(employer_id)",
    "invoice_name": "VARCHAR(255)",
    "invoice_date": "DATE",
    "invoice_company": "VARCHAR(255)"
})
