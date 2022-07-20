a = '---'
print(a*15)#line
print("Checking Your Prime Number! \n")
min = int(input("Enter your min number: " ))
max = int(input("Enter your max number: "))

amount = 0
prime = True
for num in range (min , max + 1 ):
    for i in range (2, num):
        if (num%i== 0 ):
            prime = False
            break
    if(prime):
        print(num)#print the prime number 
        amount = amount + 1 #count the length 
    prime = True
print("Your Total Prime Number: ", amount) #print out the length of the string 
print(a*15)