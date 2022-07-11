
L = [1,4,7,5,9,3,0,3,2]
for i in range(len(L)):
    for n in range(i + 1, len(L)):

        if L[i] > L[n]:
            L[i], L[n] = L[n], L[i]

print(L)

#another way 
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]
    for i in data_list:
        if minimum > i:
            minimum = i
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)
