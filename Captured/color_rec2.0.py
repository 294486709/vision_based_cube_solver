import cv2
import numpy as np
import os
w="w"
g="g"
o="o"
y="y"
b="b"
r="r"


def rec(path):
    HSV = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2HSV)
    center = []
    map = np.zeros((60,60))
    center.append([10, 10])
    center.append([7, 27])
    center.append([8, 48])
    center.append([32, 12])
    center.append([30, 30])
    center.append([30, 50])
    center.append([52, 12])
    center.append([47, 27])
    center.append([50, 50])
    margen = 0.15*255
    for k in range(1,10):
        map[center[k-1][0],center[k-1][1]] = k
        #print map[center[k-1][0],center[k-1][1]]
        upper=[0,0,0]
        lower=[0,0,0]
        current = HSV[center[k-1][0],center[k-1][1]]
        #print current
        for j in range(3):
            upper[j] = current[j] + margen
            lower[j] = current[j] - margen
        while 1:
            foundlist = []
            for i in range(60):
                for j in range(60):
                    if map[i,j] == k:
                        foundlist.append([i,j])
            nb = []
            countr = 0
            for c in foundlist:
                if c[0] == 0 and c[1] == 0:
                    count = 0
                    currenttest = HSV[c[0], c[1] + 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] + 1] == 0.0:
                        map[c[0], c[1] + 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]+1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]+1, c[1]] == 0.0:
                        map[c[0]+1, c[1]] = k
                        countr += 1

                elif c[0] == 59 and c[1] == 59:

                    count = 0
                    currenttest = HSV[c[0]-1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]-1, c[1]] == 0.0:
                        map[c[0]-1, c[1]] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0], c[1] - 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] - 1] == 0.0:
                        map[c[0], c[1] - 1] = k
                        countr += 1
                elif c[0] == 0 and c[1] == 59:
                    count = 0
                    currenttest = HSV[c[0], c[1] - 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] - 1] == 0.0:
                        map[c[0], c[1] - 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]+1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]+1, c[1]] == 0.0:
                        map[c[0]+1, c[1]] = k
                        countr += 1

                elif c[0] == 59 and c[1] == 0:
                    count = 0
                    currenttest = HSV[c[0], c[1] + 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] + 1] == 0.0:
                        map[c[0], c[1] + 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]-1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]-1, c[1]] == 0.0:
                        map[c[0]-1, c[1]] = k
                        countr += 1

                elif c[0] == 0  and c[1] <> 0:
                    count = 0
                    currenttest = HSV[c[0], c[1] + 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] + 1] == 0.0:
                        map[c[0], c[1] + 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0], c[1] - 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] - 1] == 0.0:
                        map[c[0], c[1] - 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]+1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]+1, c[1]] == 0.0:
                        map[c[0]+1, c[1]] = k
                        countr += 1

                elif c[0] == 59 and c[1] <> 0:
                    count = 0
                    currenttest = HSV[c[0], c[1] + 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] + 1] == 0.0:
                        map[c[0], c[1] + 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]-1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]-1, c[1]] == 0.0:
                        map[c[0]-1, c[1]] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0], c[1] - 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] - 1] == 0.0:
                        map[c[0], c[1] - 1] = k
                        countr += 1

                elif c[0] <> 0 and c[1] == 0:
                    count = 0
                    currenttest = HSV[c[0], c[1] + 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] + 1] == 0.0:
                        map[c[0], c[1] + 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]-1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]-1, c[1]] == 0.0:
                        map[c[0]-1, c[1]] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]+1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]+1, c[1]] == 0.0:
                        map[c[0]+1, c[1]] = k
                        countr += 1

                elif c[0] <> 0 and c[1] ==59:

                    count = 0
                    currenttest = HSV[c[0]-1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]-1, c[1]] == 0.0:
                        map[c[0]-1, c[1]] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0], c[1] - 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] - 1] == 0.0:
                        map[c[0], c[1] - 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]+1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]+1, c[1]] == 0.0:
                        map[c[0]+1, c[1]] = k
                        countr += 1

                else:
                    count = 0
                    currenttest = HSV[c[0], c[1] + 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] + 1] == 0.0:
                        map[c[0], c[1] + 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]-1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]-1, c[1]] == 0.0:
                        map[c[0]-1, c[1]] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0], c[1] - 1]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0], c[1] - 1] == 0.0:
                        map[c[0], c[1] - 1] = k
                        countr += 1

                    count = 0
                    currenttest = HSV[c[0]+1, c[1]]
                    for q in range(3):
                        if currenttest[q] <= upper[q] and currenttest[q] >= lower[q]:
                            count += 1
                    if count == 3 and map[c[0]+1, c[1]] == 0.0:
                        map[c[0]+1, c[1]] = k
                        countr += 1
            if countr == 0:
                break
    avg_HSV_T = []
    for k in range(1,10):
        similarlist=[]
        H_value = 0
        S_value = 0
        V_value = 0
        if not map[center[k-1][0],center[k-1][1]] == 0:
            currentvalue = map[center[k-1][0],center[k-1][1]]
            for i in range(60):
                for j in range(60):
                    if map[i][j] == currentvalue:
                        similarlist.append(HSV[i][j])
            totalcount = len(similarlist)
            for i in similarlist:
                H_value += i[0]
                S_value += i[1]
                V_value += i[2]
            avg_H = H_value/totalcount
            avg_S = S_value/totalcount
            avg_V = V_value/totalcount
            avg_HSV = [avg_H,avg_S,avg_V]
            avg_HSV_T.append(avg_HSV)

        else:
            print "error!"
            dd=os.system('read "Press any key to continue"')
    return avg_HSV_T,map




def writefile(map,filename):
    f = open(filename, 'w')
    for i in range(60):
        for j in range(60):
            temp = str(map[i, j])
            #print temp
            f.write(temp)
            f.write('  ')
            if j == 59:
                f.write('\n')
    f.close()


def colordef(avg_HSV,type):
    color_total = []
    if type == 1:
        lower_yellow = [26, 43, 46]
        upper_yellow = [38, 255, 255]
        lower_red = [0, 160, 46]
        upper_red = [10, 255, 255]
        lower_blue = [100, 43, 46]
        upper_blue = [124, 255, 255]
        lower_green = [39, 43, 46]
        upper_green = [77, 255, 255]
        lower_white = [0, 0, 211]
        upper_white = [180, 30, 255]
        lower_orange = [0, 43, 46]
        upper_orange = [25, 159, 255]
    elif type ==2:
        lower_yellow = [26, 43, 46]
        upper_yellow = [38, 255, 255]
        lower_red = [0, 160, 46]
        upper_red = [10, 255, 255]
        lower_blue = [100, 43, 46]
        upper_blue = [124, 255, 255]
        lower_green = [39, 43, 46]
        upper_green = [77, 255, 255]
        lower_white = [0, 0, 211]
        upper_white = [180, 30, 255]
        lower_orange = [0, 43, 46]
        upper_orange = [25, 159, 255]
    else:
        lower_yellow = [26, 37, 46]
        upper_yellow = [38, 255, 255]
        #lower_red = [0, 160, 46]
        #upper_red = [10, 255, 255]
        lower_blue = [100, 43, 46]
        upper_blue = [124, 255, 255]
        lower_green = [39, 43, 46]
        upper_green = [82, 255, 255]
        lower_white = [0, 0, 190]
        upper_white = [180, 30, 255]
        lower_orange = [0, 43, 151]
        upper_orange = [25, 159, 255]
        lower_red = [0, 43, 46]
        upper_red = [25, 159, 150]
        upper_red1 = [185,180,150]
        lower_red1 = [160,100,46]
    for i in avg_HSV:
        color = 'error!'
        counter_temp = 0
        for j in range(3):
            if lower_yellow[j] <= i[j] & i[j] <= upper_yellow[j]:
                counter_temp += 1
        if counter_temp == 3:
            color = 'yellow'
            color_total.append(color)
            continue
        counter_temp = 0
        for j in range(3):
            if lower_red[j] <= i[j] & i[j] <= upper_red[j]:
                counter_temp += 1
        if counter_temp == 3:
            color = 'red'
            color_total.append(color)
            continue
        counter_temp = 0
        if type == 3:
            for j in range(3):
                if lower_red1[j] <= i[j] & i[j] <= upper_red1[j]:
                    counter_temp += 1
            if counter_temp == 3:
                color = 'red'
                color_total.append(color)
                continue

        counter_temp = 0
        for j in range(3):
            if lower_white[j] <= i[j] & i[j] <= upper_white[j]:
                counter_temp += 1
        if counter_temp == 3:
            color = 'white'
            color_total.append(color)
            continue
        counter_temp = 0
        for j in range(3):
            if lower_orange[j] <= i[j] & i[j] <= upper_orange[j]:
                counter_temp += 1
        if counter_temp == 3:
            color = 'orange'
            color_total.append(color)
            continue
        counter_temp = 0
        for j in range(3):
            if lower_blue[j] <= i[j] & i[j] <= upper_blue[j]:
                counter_temp += 1
        if counter_temp == 3:
            color = 'blue'
            color_total.append(color)
            continue
        counter_temp = 0
        for j in range(3):
            if lower_green[j] <= i[j] & i[j] <= upper_green[j]:
                counter_temp += 1
        if counter_temp == 3:
            color = 'green'
            color_total.append(color)
            continue
        color_total.append(color)
    return color_total

def main():
    path1 = 'pside1.jpg'
    path2 = 'pside2.jpg'
    path3 = 'pside3.jpg'
    path4 = 'pside4.jpg'
    path5 = 'pside5.jpg'
    path6 = 'pside6.jpg'
    type = 1

    avg_HSV, map = rec(path1)
    writefile(map, path1 + '.txt')
    print avg_HSV
    color1 = colordef(avg_HSV, 3)
    print color1
    print '---------------------------------------------'
    avg_HSV, map = rec(path2)
    writefile(map, path2 + '.txt')
    print avg_HSV
    color2 = colordef(avg_HSV, 3)
    print color2
    print '---------------------------------------------'
    avg_HSV, map = rec(path3)
    writefile(map, path3 + '.txt')
    print avg_HSV
    color3 = colordef(avg_HSV, 3)
    print color3
    print '---------------------------------------------'
    avg_HSV, map = rec(path4)
    writefile(map, path4 + '.txt')
    print avg_HSV
    color4 = colordef(avg_HSV, 3)
    print color4
    print '---------------------------------------------'
    avg_HSV, map = rec(path5)
    writefile(map, path5 + '.txt')
    print avg_HSV
    color5 = colordef(avg_HSV, 3)
    print color5
    print '---------------------------------------------'
    avg_HSV, map = rec(path6)
    writefile(map, path6 + '.txt')
    print avg_HSV
    color6 = colordef(avg_HSV, 3)
    print color6
    print '---------------------------------------------'
    result1 = []
    result1.append(color1)
    result1.append(color2)
    result1.append(color3)
    result1.append(color4)
    result1.append(color5)
    result1.append(color6)
    result2 = []
    for i in result1:
        ttemp = []
        for j in i:
            if j == 'yellow':
                ttemp.append(y)
            elif j == 'red':
                ttemp.append(r)
            elif j == 'white':
                ttemp.append(w)
            elif j == 'green':
                ttemp.append(g)
            elif j == 'blue':
                ttemp.append(b)
            elif j == 'orange':
                ttemp.append(o)
            else:
                print "error!"
        result2.append(ttemp)
    print result2
    f = open('resulti.txt','a')
    for i in result2:
        for j in i:
            f.write(j)
        f.write('\n')
    f.close()
    return result2
'''    
    filename = path1 + 'txt'
    writefile(map,filename)
    map = rec(path2,type)
    filename = path2 + 'txt'
    writefile(map,filename)
    map = rec(path3,type)
    filename = path3 + 'txt'
    writefile(map,filename)
    map = rec(path4,type)
    filename = path4 + 'txt'
    writefile(map,filename)
    map = rec(path5,type)
    filename = path5 + 'txt'
    writefile(map,filename)
    map = rec(path6,type)
    filename = path6 + 'txt'
    writefile(map,filename)
'''


if __name__ == '__main__':
    main()