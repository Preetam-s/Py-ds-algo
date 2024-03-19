# Print the sum of factors

noOfElements = int(input("Enter the number of elements: "))
k_Elm = []
output = []

for i in range(0,noOfElements):
    elm = int(input())
    k_Elm .append(elm)



def calculateSumFactors(k):
    #print(k)
    sum = 0
    for j in range(1,i//2+1):
        if(i%j==0):
            sum = sum +j
    sum = sum + i
    output.append(sum)
    return output

for i in k_Elm:
    x = calculateSumFactors(k_Elm)
print (x)