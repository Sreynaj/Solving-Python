a = '---'
print(a*15)#line
#ask the user to enter the input
FC = int(input("\nHow many terms do you want to print?: "))

#first two terms
n1=0
n2=1
count=0
FB = []

while count < FC:
    #print(n1)
    n12= n1 + n2
 # At last, we will update values  
    n1 = n2
    n2 = n12
    count += 1
    FB.append(n1)
print("\nThe fibonacci sequence of the numbers:\n", FB)
print(a*15)