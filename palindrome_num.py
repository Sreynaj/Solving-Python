a = '--'
print(a*15)#line
numbers = int(input("Enter Your Numbers: "))
reverse = 0
palin = int(numbers)
while numbers > 0 :
    reverse = (reverse*10) + (numbers %10)
    numbers = numbers // 10
print("\nYour Reverse Numbers:",reverse)
#find palindrome numbers
if palin == reverse:
    print("\n",palin,"And",reverse,"Are Palindrome Numbers ")
else: 
    print("\n",palin,"And",reverse,"Are Not Palindrome numbers")

print(a*15)#line