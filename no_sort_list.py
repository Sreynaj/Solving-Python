L = [1,4,7,5,9,3,0,3,2]
for i in range(len(L)):
    for n in range(i + 1, len(L)):

        if L[i] > L[n]:
            L[i], L[n] = L[n], L[i]

print(L)