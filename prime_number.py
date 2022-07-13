print("\nChecking Your Prime Number! \n")
min = int(input("Enter your min number: " ))
max = int(input("Enter your max number: "))

#find the prime number in min-max
print("\nYour Prime Numbers Are: ")
L = []
for i in range (min ,max+1):
    if i > 1: #prime number
        for num in range(2,i): 
            if (i %num)== 0:
                break
        else:
            L.append(i)
print(L)

#count the legnth of string
n=0
for i in L:
    n = n + 1
print("\nYour Total Prime Number: ", n)

