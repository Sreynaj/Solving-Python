a = '---'
print(a*15)#line
print("Find A Position Of Numbers! \n")
min = int(input("Enter your min number: " ))
max = int(input("Enter your max number: "))

number=[]
for i in range(min,max + 1):
    number.append(i)
print("Your Number:\n",number)

find = int(input("\nEnter a number to find its position: "))
print(a*15)
for i in range (len(number)):
    if number[i] == find:
        print("Found it in position",i)

print(a*15)
