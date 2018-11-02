f = open('resulti.txt', 'r')
colors = []
for i in range(6):
    colors.append(f.readline(12).replace('\n',''))
importedcolor = []
for i in colors:
    tempp = []
    for j in i:
        tempp.append(j)
    importedcolor.append(tempp)
print importedcolor