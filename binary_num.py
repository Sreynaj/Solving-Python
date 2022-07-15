a = '---'
print(a*15)#line
number = int(input("Enter Your Number: "))
while number != 0:
    remainder = number % 10
    if (remainder != 0 and remainder != 1 ):
        print("The string is not a binary number!")
        break
    number = number // 10
    if (number == 0):
        print("\nThe string is a binary number!")
print(a*15)#line