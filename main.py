#coding=utf-8
import solver as sv
import Cube_simulator as cs
import sys

w="w"
g="g"
o="o"
y="y"
b="b"
r="r"

#red = [b,y,b,b,r,b,b,y,b]
#orange = [g,w,g,g,o,g,g,w,g]
#white = [y,g,y,y,w,y,y,g,y]
#yellow = [w,b,w,w,y,w,w,b,w]
#blue = [r,r,r,r,b,r,r,r,r]
#green = [o,o,o,o,g,o,o,o,o]


def solver1(white,blue,red,yellow,green,orange):
    sortedall = []
    sortedall.append(white)
    sortedall.append(blue)
    sortedall.append(red)
    sortedall.append(yellow)
    sortedall.append(green)
    sortedall.append(orange)
    cubestring =""
    for k in sortedall:
        for i in k:
            if i == "w":
                str1 = "".join("U")
            elif i == "r":
                str1 = "".join("F")
            elif i == "y":
                str1 = "".join("D")
            elif i == "b":
                str1 = "".join("R")
            elif i == "o":
                str1 = "".join("B")
            else:
                str1 = "".join("L")
            cubestring += str1


    #cubestring = "RDBFULRRFLUDFRURLFUBUFFRURULDFUDBLUDBLBDLDDRBLLDFBBRBF"
    res = sv.solve(cubestring,1,1)
    f = open("result.txt","w")
    i=0
    inst=[]
    while (i) <= (len(res)-2):######################################################
        f.write(res[i]+res[i+1]+"\n")
        inst.append(res[i]+res[i+1])
        i+=3
    f.close()
    #print(inst)
    return inst


def main():
    f = open('resulti.txt', 'r')
    colors = []
    for i in range(6):
        colors.append(f.readline(12).replace('\n', ''))
    importedcolor = []
    for i in colors:
        tempp = []
        for j in i:
            tempp.append(j)
        importedcolor.append(tempp)
    orange = importedcolor[0]
    yellow = importedcolor[1]
    white = importedcolor[2]
    red = importedcolor[3]
    blue = importedcolor[4]
    green = importedcolor[5]
    f.close()

    cs.display(red, orange, white, yellow, blue, green,"w")
    instrucion = solver1(white,blue,red,yellow,green,orange)
    list1=[]
    list2=[]
    for i in instrucion:
        if i[0] == "U":
            dir = "w"
        elif i[0] == "F":
            dir = "r"
        elif i[0] == "D":
            dir = "y"
        elif i[0] == "R":
            dir = "b"
        elif i[0] == "B":
            dir = "o"
        else:
            dir = "g"
        if i[1]=="1":
            list1.append(dir)
            list2.append(1)
        elif i[1]=="2":
            list1.append(dir)
            list1.append(dir)
            list2.append(1)
            list2.append(1)
        else:
            list1.append(dir)
            list2.append(-1)
    for i in range(len(list1)):
        red, orange, white, yellow, blue, green = cs.trans(red, orange, white, yellow, blue, green, list1[i], list2[i])

    for i in range(len(list1)):
        print(list1[i],list2[i])
    f = open('instructions.txt','w')
    for i in range(len(list1)):
        f.write(str(list1[i]))
        f.write('\n')
        f.write(str(list2[i]))
        f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
