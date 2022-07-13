print("\nFind A Position Of Numbers! \n")
min = int(input("Enter your min number: " ))
max = int(input("Enter your max number: "))

number=[]
for i in range(min,max + 1):
    number.append(i)
print(number)

find = int(input("\nEnter a number to find its position:"))
for i in range (len(number)):
    if number[i] == find:
        print("Found it in position",i)

