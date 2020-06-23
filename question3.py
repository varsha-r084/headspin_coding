__author__ = 'VARSHA'

N = int(input("Enter the end number : "))
sum = 0

for num in range(1,N+1):
    fact = 1
    div = 1
    for x in range(1,N+1):
        fact = fact * x
    #print fact
    num1 = float(num)
    fact1 = float(fact)
    div = num1/fact1
    #print div
    sum = sum + div
print("Sum of the sequense is : "+str(sum))