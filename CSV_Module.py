import csv
# Open file
data = open('example.csv',encoding ="utf-8")

#csv.reader
csv_data = csv.reader(data)

# reformat it into a pythin object List of list
data_lines = list(csv_data)
all_emails = []
for lines in data_lines[1:]:
    all_emails.append(lines[3])

full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+" "+line[2])
print((full_names))


## WRITING TO CSV FILE ##
# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'.
file_to_output = open('to_save_file.csv','w',newline='')

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()
# Existing File

f = open('to_save_file.csv','a',newline='')

csv_writer = csv.writer(f)

csv_writer.writerow(['new','new','new'])

f.close()
