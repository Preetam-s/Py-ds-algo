class Book(object):
	"""docstring for Book"""
	def __init__(self, title, author, pages):
		
		self.title = title
		self.author = author
		self.pages = pages

	# String Representation of a Class

	def __str__(self):
		return f"{self.title} by {self.author}"

	def __len__(self):
		return self.pages

b = Book("Python","Jose",200)
print(b)

print(len(b))

##################### Object oriented Programing Homework ########################
### Problem 1 #############

class Line(object):
	"""docstring for Line"""
	def __init__(self, coor1,coor2):
		#super(Line, self).__init__()
		self.coor1 = coor1
		self.coor2 = coor2
	def distance(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return ((x2-x1)**2 + (y2-y1)**2)**0.5
	def slope(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

### Problem 2 ##################

class Cylinder(object):
	"""docstring for ClassName"""
	pi = 3.14
	def __init__(self,height=1,radius=1):
		#super(ClassName, self).__init__()
		self.height = height
		self.radius = radius
	def volume(self):
		return self.pi*self.radius**2*self.height
	def surface_area(self):
		return  2*self.pi*self.radius*self.height + 2*self.pi*self.radius**2

c = Cylinder(2,3)

print(c.volume())

print(c.surface_area())

################# CHALLANGE 1 #################

class Account(object):
	"""docstring for Accout"""
	def __init__(self, owner,balance):
		#super(Accout, self).__init__()
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f"Accout Owner : {self.owner} \nAccout Balance : {self.balance}"




	def deposit(self,sum):
		self.balance= self.balance + sum
		print("Deposit Accepted")

		
	def withdrawn(self,amt):
		if amt <= self.balance:
			self.balance = self.balance-amt
			print("Withdrawl Accepted!")
		else:
			print("Insufficient Funds!")


acct1 = Account('Jose',100)

print(acct1)
print(acct1.owner)		
print(acct1.balance)
acct1.deposit(50)
acct1.withdrawn(75)
acct1.withdrawn(500)
print(acct1)