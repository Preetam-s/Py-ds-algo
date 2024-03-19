def ask_for_int():
	while True:
		try:
			number = int(input("Please provide a number:"))
		
		except :
			print(" Whoopsie !! , not a number :(")
			continue
		else:
			print("Thank You, Input is a number!!")
			break
		finally:
			print("I shall always run!")



############# Errors and Exceptions Homework ####################

########### Problem 1 ##############

try:
	for i in ['a','b','c']:
		print(i**2)
 
except TypeError:
	print("Whoopsie type error!")

############## Problem 2 ##########
try:
 	x=5
 	y=0
 	z=x/y
except ZeroDivisionError:
 	print("Sorry! division by zero not defined")
finally:
 	print("I run !")

 ################ Problem 3 ########

def ask():

	while True:

		try:

			result = int(input("Input an Integer"))

		except:

			print("An error occured! Please try again!")
			continue

		else:

			break

	print("Thank you, number squared is:"+ result**2)


print(ask())