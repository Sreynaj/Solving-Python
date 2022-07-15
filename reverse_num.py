a = '--'
print(a*15)
numbers = int(input("Enter Your Numbers: "))
reverse = 0
while numbers > 0 :
    reverse = (reverse*10) + (numbers %10)
    numbers = numbers //10
print("\nYour Reverse Numbers:",reverse)
print(a*15)