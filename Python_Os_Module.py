import os
os.getcwd()
#C:\Users\preet\OneDrive\Desktop\PS Works\Python Practise
os.listdir()
# ['Blackjack_Game.py', 'Error and Exception Handling.py', 'generators homework.py', 'methods and functions.py', 'MyModule.py', 'MyProgram.py', 'OOP Practise.py', 'OOP.py', 'pylintoverview.py', 'Python Demo.py', 'python_decorators.py', 'Python_Os_Module.py', 'ran.py', 'shuffle_game.py', 'Statements_Assesment.py']
# lists files in current directory
os.listdir("C:\\Users\\preet\\OneDrive\\Desktop")
# lists the files given in the directory mentioned in the string

##################-----------------------------------------########################
### openfile and write to it
f=open('practise1.txt','w+')
f.write('Hello boys')
f.close()

########----------- shutil can be used to move files between directories ########

import shutil
print(os.getcwd())
# shutil.move('practise1.txt','C:\\Users\\preet\\OneDrive\\Desktop')
# print(os.listdir('C:\\Users\\preet\\OneDrive\\Desktop'))

#########deleting files usinf send2trash 3########
#  shutil.move('C:\\Users\\preet\\OneDrive\\Desktop\\practise1.txt',os.getcwd())
print(os.listdir())
import send2trash
 # send2trash.send2trash('practise1.txt')  #### goes to recycle bin 

##### walk through folders and subfoldersand list their files #####
 for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    