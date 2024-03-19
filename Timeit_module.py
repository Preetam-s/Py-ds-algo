import timeit
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'
print(timeit.timeit(stmt,setup,number= 10000))

setup1 ='''
def func_two(n):
	return list(map(str,range(n)))
'''
stmt2= 'func_two(100)'
print(timeit.timeit(stmt2,setup1,number= 10000))
