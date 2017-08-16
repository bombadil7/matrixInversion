listoflists = []
for i in range(0,2):
    sublist = []
    for j in range(0,3):
        sublist.append(i*j)
#sublist.append((i,j))
    listoflists.append(sublist)
print(listoflists)
