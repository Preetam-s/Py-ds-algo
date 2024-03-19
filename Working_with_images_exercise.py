from PIL import Image
mask = Image.open('mask.png')
word_matrix =Image.open('word_matrix.png')
print(word_matrix.size)
print(mask.size)
mask = mask.resize((1015,559))
print(mask.size)
mask.putalpha(128)
word_matrix.paste(im=mask,box=(0,0),mask=mask)
word_matrix.show()