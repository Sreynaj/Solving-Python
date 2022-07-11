print("\nChecking Your Prime Number! \n")
min = int(input("Enter your min number: " ))
max = int(input("Enter your max number: "))
amount = 0
prime = True
for num in range (min , max + 1):
    if num > 1:

        for i in range (2, num):
            if (num%i== 0 ):
                 prime = False
                 break
    if(prime):
        print(num)
        amount = amount + 1
        prime = True
print(amount)