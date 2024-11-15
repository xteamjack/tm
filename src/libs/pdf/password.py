test_file="D:/wspc3/github/Samples/resumes/Testing/UIUX_Resume1.pdf"

# pdf_encryption.py

from PyPDF2 import PdfReader, PdfWriter
reader = PdfReader(test_file)

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("junkinfo")
writer.write(test_file)