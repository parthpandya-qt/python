from pypdf import PdfReader, PdfWriter

pdf_writer = PdfWriter()

# Append first.pdf
reader1 = PdfReader("first.pdf")
for page in reader1.pages:
    pdf_writer.add_page(page)

# Append second.pdf
reader2 = PdfReader("second.pdf")
for page in reader2.pages:
    pdf_writer.add_page(page)

# Write merged output
with open("merged.pdf", "wb") as f:
    pdf_writer.write(f)
