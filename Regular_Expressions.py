text = 'my phone once, my phone twice'
pattern = 'phone'
import re
match1 = re.search(pattern,text)
print(match1)
match2 =  re.findall(pattern,text)
print(match2)

for match in re.finditer(pattern,text):
	print(match)

text1 = 'Myphone number is 408-555-7777'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text1)
print(phone)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resul = re.search(phone_pattern,text1)
print(resul.group())
print(resul.group(1))
print(resul.group(2))

print(re.search(r'cat|dog', 'The cat is here'))
print(re.findall(r'...at', 'The cat in the hat went splat')) # The . is a identifier it denotes the number of characters it will grab before the give pattern
print(re.findall(r'\d$', 'The cnumer is 2'))
print(re.findall(r'^\d', '2 The cnumer is'))
