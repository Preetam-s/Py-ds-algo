workhours = [('able',600),('babe',300),('cabe',200)]

def emp_of_month(workhours):
	
	cur_max= 0
	curr_emp=''
	for name, hours in workhours:
		if hours > cur_max:
			cur_max = hours
			curr_emp = name
		else:
			pass
	return (curr_emp,cur_max)

name1,Hours1 = emp_of_month(workhours)
print(name1)
print(Hours1)
###############################################
def myFunc(*args):
	return sum(args)*0.5

print(myFunc(2,3,4,6,7,8))

def ffmy(**kwargs):
	print(kwargs)
	if 'fruit'in kwargs:
		print('My fruit of choice id {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')

print(ffmy(fruit='apple',veggie='lettuce'))

###############################
def myfunc69(args):
    str1=[]
    for i in range(len(args)):
        if i%2==0:
            str1.append(args[i].lower())
        else:
            str1.append(args[i].upper())
    
    return ''.join(str1)

print(myfunc69("hellobabies"))
def myfunc23(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

print(myfunc23("hellobabies"))

#########3 LESSER OF TWO EVENS ###########
def lesser_of_two_evens(a,b):
	if a%2==0 and b%2==0:
		if a<b:
			return a
		else:
			return b
	elif a%2!=0 or b%2!=0:
		if a>b:
			return a
		else:
			return b
	else:
			pass
		
		
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(7,5))

############# ANIMAL CRACKERS ###########
def animal_crackers(text):
 	 wordlist = text.lower().split()
 	 first = wordlist[0]
 	 second = wordlist[1]

 	 return first[0]==second[0]

print(animal_crackers('Hello lippie'))

############ MAKES TWENTY ########
def makes_twenty(n1,n2):
	return n1+n2==20 or n1==20 or n2==20
		
print(makes_twenty(20,10))
print(makes_twenty(2,3))

############ OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name #########
def old_macdonld(text):
	a = text[0].upper()
	b = text[3].upper()
	return a+text[1:3]+b+text[4:]
##### ALter Solution #####
def old_macdonld2(text):
	a = text[:3]
	b = text[3:0]
	return a.capitalize()+b.capitalize()
print(old_macdonld("macdonald"))
print(old_macdonld2("Preetam"))
 
#################### MASTER YODA: Given a sentence, return a sentence with the words reversed ############
def master_yoda(text):
	wordlist = text.split()
	reverse_wordlist = wordlist[::-1]
	return ' '.join(reverse_wordlist)
 
print(master_yoda('hello Boys'))

############# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200 ########
def almost_there(n):
	x = 100-n 
	y = 200-n
	if abs(x)<=10:
		return True
	elif abs(y)<=10:
		return True
	else:
		return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print("\n")	
########## FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere. ######
def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i]==3 and nums[i+1]==3:
			return True
	return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))

#############PAPER DOLL: Given a string, return a string where for every character in the original there are three characters #######

def paper_doll(text):
	result=""
	for i in text:
		result = result + i*3
	return result
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

###################3BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'###3

def blackjack(a,b,c):
	if a+b+c <= 21:
		return a+b+c
	elif a+b+c > 21:
		if a==11 or b==11 or c==11:
			return a+b+c - 10
		else:
			return "BUST"

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

def blackjack2(a,b,c):
	if sum ([a,b,c])<= 21:
		return sum ([a,b,c])
	elif 11 in [a,b,c] and sum([a,b,c])<=31:
		return sum([a,b,c])-10
	else:
		return "BUST"	
print(blackjack2(5,6,7))
print(blackjack2(9,9,9))
print(blackjack2(9,9,11))

########### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.#######

def summer_69(arr):
	sum=0
	add =  True
	for num in arr:
		while add:
			if num!=6:
				sum = sum +num
				break
			else:
				add= False
		while not add:
			if num!=9:
				break
			else:
				add = True
				break
	return sum
			
############ SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order ####3
def spy_game(nums):

	code = [0,0,7,'x']

	for num in nums:
		if num == code[0]:
			code.pop(0)

	return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

############ COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number########

def count_primes(n):
	count =0
	for num in range(n):
		if num <=1:
			continue
		for i in range(2, num):
			if(num%i)==0:
				break
		else:
			count = count + 1
	return count

print(count_primes(100))

############ Fuction for volume of sphere #####3

def vol(rad):
	return (4/3)*3.14*rad**3

print(vol(2))

################# Number is in given range ############
def ran_check(num, low , high):
	if num>=low and num <=high:
		return '{} is in the range between {} and {}'.format(num,low,high)
	else:
		return False
print(ran_check(5,3,7))
print(ran_check(3,1,10))
print(ran_check(7,1,5))

def ran_bool(num, low , high):
	return num>=low and num <=high

print(ran_bool(5,3,7))
print(ran_bool(3,1,10))
print(ran_bool(7,1,5))

################ number of uppercase and lowercase #########
def up_low(s):
	lowercase= 0
	uppercase=0

	for char in s:
		if char.isupper():
			uppercase+=1
		elif char.islower():
			lowercase+=1
		else:
			pass
	print(f"Original string: {s}")
	print(f'Uppercase Count: {uppercase}')
	print(f'lowercase Count: {lowercase}')
print(up_low('Hello teegr dffdDFdfSAAfg'))

################ Function that returns unique elements in a list #########
def unique_list(lst):
	new_lst = [set(lst)]
	return new_lst
print(unique_list([1,11,1,1,2,2,3,4,5,3,21,1,2,3,4,5,5,5]))

################ Multiply all numbers in a List ################
def multiply(numbers):
	pro = 1
	for num in numbers:
		pro = pro * num
	return pro

print(multiply([1,2,3,-4]))

############## Check Palindrome ##################
def palindrome(s):
	#remove spaces
	s= s.replace(' ','')

	#check if reverse of string is equal to original
	rev_s = s[::-1]
	return s == rev_s

print(palindrome('nitin'))
print(palindrome('God Save the queen'))
print(palindrome('nurses run'))

################ check if a string , is a pangram ########
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
	# create a set of the alphabets
	alphaset = set(alphabet)
	# Remove spaces from input string
	str1 = str1.replace(' ','')
	#Convert into lower case
	str1 = str1.lower()
	# Grab unique letters from input string
	str1 = set(str1)
	# check if alphabet set  == string set input
	return str1 == alphaset
print(ispangram("The quick brown fox jumps over the lazy dog"))

	

