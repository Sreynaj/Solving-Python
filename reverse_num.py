a = '--'
print(a*15)#line
numbers = int(input("Enter Your Numbers: "))
reverse = 0
while numbers > 0 :
    reverse = (reverse*10) + (numbers %10)
    numbers = numbers // 10
print("\nYour Reverse Numbers:",reverse)
print(a*15)#line

#another way 
number = input("Type Your Number: ")
last_index = number[::-1]
print("\nYour Reverse Numbers:",last_index)
print(a*15)#line