def hello (name ='jose'):
	print("this is the hello() function")
	def greet():
		return ("\t this is the greet function ")
	def welcome():
		return ('\t this welcome() inside hello()')

	print('I m going to return a function')

	if name =='Jose':
		return greet
	else:
		return welcome

my_new_func = hello()
print(my_new_func())

def cool():
	def super_cool():
		return ' I am very cool! '
	return super_cool
some_func = cool()
print(some_func())

def hello1():
	return 'Hi Jose'
def other(some_def_func):
	print('some code ........')
	print(some_def_func())

print(other(hello1))

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

print(func_needs_decorator())