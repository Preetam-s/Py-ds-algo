
# Print the count of Evens in a the input list 

input_str = input("Enter elements of the list separated by space: ")  
  
# Converting input string to a list of integers  
my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

count = 0
for i in my_list:
    if i % 2 == 0:
        count = count +1 

print("Count of Evens : ",count)

