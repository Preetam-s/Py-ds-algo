import csv,PyPDF2,re
data = open('find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_str = ''
for row,data in enumerate(data_lines):
    link_str += data[row]
print(link_str)

f = open('Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
pdf.numPages
pattern = r'\d{3}'
all_text = ''
for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()
    all_text = all_text+' '+page_text
for match in re.finditer(pattern,all_text):
    print(match)
print(all_text[41790:41820])