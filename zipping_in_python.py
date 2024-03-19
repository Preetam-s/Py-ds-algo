'''
f = open('fileone.txt','w+')
f.write('FILE ONE')
f.close()

e = open('filetwo.txt','w+')
e.write('FILE TWO')
e.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.close ()
'''
import zipfile
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')