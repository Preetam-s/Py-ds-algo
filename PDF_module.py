import PyPDF2
'''
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages

first_page = pdf_reader.getPage(0)
first_page_text = first_page.extractText()
print(first_page_text)
f.close()'''
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)

f.close()

f = open('Working_Business_Proposal.pdf', 'rb')

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)

    pdf_text.append(page.extractText())

print(pdf_text[3])