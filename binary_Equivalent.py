a = '--'
print(a*15)#line
print("\tBINARY EQUIVALENT")
number = int(input("Enter Your Number: "))
list = []
while(number>0):
    d = number%2
    list.append(d)
    number = number//2
list.reverse()
print("Binary Equivalent is: ")
for i in list:
    print(i,end = '')
print()
print(a*15)#line
