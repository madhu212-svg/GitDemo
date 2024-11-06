import re
import PyPDF2

def extract_emails_from_pdf(pdf_path):  # Corrected function parameter
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        emails = []

        # Iterate through all the pages of the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()

            # Regular expression to match emails ending with '.com'
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
            found_emails = re.findall(email_pattern, text)
            emails.extend(found_emails)

    return emails

# Specify the correct PDF file path
pdf_path = 'C:/Users/m/Desktop/interview prep/Pune Mumbai.pdf'  # Correct the file path to your actual PDF

# Call the function with the correct path
emails = extract_emails_from_pdf(pdf_path)

# Display the extracted emails
for email in emails:
    print(email)
