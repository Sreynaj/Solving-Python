a = "---"
print(a*15)
L = [1,4,7,5,9,3,0,3,2]
print("List:",L)
for i in range(len(L)):
    #accending
    for n in range(i + 1, len(L)):

        if L[i] > L[n]:
            L[i], L[n] = L[n], L[i]
print("Accending: ", L)
#decending
for i in range(len(L)):
    for n in range(i + 1, len(L)):
    
        if L[i] < L[n]:
            L[i], L[n] = L[n], L[i]
print("Decending: ", L)

#another way 
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
print("\nList:", data_list)
new_list = []

while data_list:
    minimum = data_list[0]
    for i in data_list:
        if minimum > i: #min < i: accending, min > i :decending
            minimum = i
    new_list.append(minimum)
    data_list.remove(minimum)
print("Accending: " , new_list)
while data_list:
    minimum = data_list[0]
    for i in data_list:
        if minimum < i: #min < i: accending, min > i :decending
            minimum = i
    new_list.append(minimum)
    data_list.remove(minimum)
print("Decending: " , new_list)
print(a*15)