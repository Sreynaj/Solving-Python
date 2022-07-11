print("\nChecking Your Prime Number! \n")
min = int(input("Enter your min number: " ))
max = int(input("Enter your max number: "))

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
