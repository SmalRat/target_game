mas = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
mas1 = []
for i in range(len(mas[0])):
    mas1.append([])
    for j in range(len(mas)):
        mas1[i].append(mas[j][i])
print(mas1)