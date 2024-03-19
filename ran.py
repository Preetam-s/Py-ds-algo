#str='hello'
#print(str[::-1])
#list1= [1,2,[3,3,'hello']]
#list1[2][2]='goodbye'
#print(list1)
#d={'k1':{'k2':'hello'}}
#print(d['k1']['k2'])
#d={'k1':[{'nest_key':['this is deep',['hello']]}]}
#print(d['k1'][0]['nest_key'][1][0])
##
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print(d['k1'][2]['k2'][1]['tough'][2][0])

#mylist=[ x**3 for x in range(0,11) ]
#print(mylist)

#1
st1 = 'Print only the words that start with s in this sentence'
for word in st1.split():
    if word[0] == 's':
        print(word)


print('\n')
#2
for x in range(0,11):
	if x%2==0:
		print(x)
my=list(range(0,11,2))
print(my)
print('\n')



#3
mylist = [x for x in range(1,51) if x%3==0]
print(mylist)
print('\n')
#4
st2 = 'Print every word in this sentence that has an even number of letters'
for word in st2.split():
    if len(word)%2==0:
        print(word)
print('\n')
#5
for x in range (1,101):
	if x%3==0 and x%5!=0:
		print('fizz')
	elif x%5==0 and x%3!=0:
		print('buzz')
	elif x%3==0 and x%5==0:
		print('fizzbuzz')
	else:
		print(x)

print('\n')

#6
st6 = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st6.split()])