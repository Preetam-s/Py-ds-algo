##### Math Module #######

import math
val = 4.35
print(math.floor(val))
print(math.ceil(val))
print(round(val))
print(math.pi)
print(math.e)
print(math.log(math.e))
print(math.log(100,10))

######## Random Module ##########
import random
x = random.randint(0,100)
print(x)

random.seed(101)  ## setting  seed enables us to get consistent random values across diverent environmrnts
y = random.randint(0,100)
print(y)
a =random.randint(0,100)
print(a)
mylist = list(range(0,20))
print(mylist)
r = random.choice(mylist)
print(r)
print('\n')
 # Choosing n random nymbers from a list with replacement 
list1 = random.choices(population = mylist, k=10)
print(f"{list1}\n")

# choosing n random numbers  from a list without replacement (without duplication)
list2 = random.sample(population = mylist, k=10)
print(list2)