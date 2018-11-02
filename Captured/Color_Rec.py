import cv2
import numpy as np
import time
import sys

def find9(total_contour):
    size9 = []
    thread1=0
    for i in total_contour:
        size9.append(i.size)
    while 1:
        size9.sort()
        size9.reverse()
        sizetemp = [0] * 9
        for i in range(9):
            sizetemp[i] = size9[i]
        avg = sum(sizetemp)/9
        #if 0.7 < float(size9[0])/float(size9[1]) < 1.3 and 0.7 < float(size9[1])/float(size9[2]) < 1.3 and 0.7 < float(size9[2])/float(size9[3]) < 1.3:
        theard = size9[8] - 1
        thread1 = size9[0] + 1
        break
#        size9[0] = thread1
#        size9[0] = 0
    if thread1 == 0:
        thread1 = 99999999999
    return theard,thread1


def sortcoord(a):
    # init variable
    result = []
    temp =[]
    l = len(a)
    # sort by Y



    for i in range(l):
        j = i
        for j in range(i, l):
            if (a[i][1] > a[j][1]):
                a[i], a[j] = a[j], a[i]
        # geather temp result
    for k in range(len(a)):
        temp.append(a[k])
        # split temp
    temp_1 = temp[0:3]
    temp_2 = temp[3:6]
    temp_3 = temp[6:9]
    # sort within 3 by x
    for i in range(0, 3):
        j = i
        for j in range (i, 3):
            if (temp_1[i][0] > temp_1[j][0]):
                temp_1[i], temp_1[j] = temp_1[j], temp_1[i]

    for i in range(0, 3):
        j = i
        for j in range (i, 3):
            if (temp_2[i][0] > temp_2[j][0]):
                temp_2[i], temp_2[j] = temp_2[j], temp_2[i]

    for i in range(0, 3):
        j = i
        for j in range (i, 3):
            if (temp_3[i][0] > temp_3[j][0]):
                temp_3[i], temp_3[j] = temp_3[j], temp_3[i]
        # write return
    for i in range(0, 3):
        result.append(temp_1[i])

    for i in range(0 ,3):
        result.append(temp_2[i])

    for i in range(0,3):
        result.append(temp_3[i])
    return result








def rec(lmg_path):
    # load image file
    Img = cv2.imread(img_path)
    # init kernel
    kernel_4 = np.ones((4, 4), np.uint8)
    #kernel = np.ones((4, 4), np.float32)/25
    #Img = cv2.filter2D(Img, -1, kernel)
    #cv2.imshow("1", Img)
    #K= cv2.waitKey(0)
    if Img is not None:
        # RGB - HSV
        HSV = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)
        # date for color rec
        lower_yellow = np.array([26, 43, 46])
        upper_yellow = np.array([34, 255, 255])
        lower_red = np.array([0, 160, 46])
        upper_red = np.array([10, 255, 255])
        lower_blue = np.array([100, 43, 46])
        upper_blue = np.array([124, 255, 255])
        lower_green = np.array([35, 43, 46])
        upper_green = np.array([77, 255, 255])
        lower_white = np.array([0, 0, 211])
        upper_white = np.array([180, 30, 255])
        lower_orange = np.array([0, 43, 46])
        upper_orange = np.array([25, 159, 255])
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 46])
        coord_yellow = []
        coord_red = []
        coord_blue = []
        coord_green = []
        coord_orange = []
        coord_white = []
        key = []
        total_coord = []
        index_color = [0] * 9
        idx_yellow =[]
        idx_red = []
        idx_orange = []
        idx_blue = []
        idx_green = []
        idx_white = []

        font = cv2.FONT_HERSHEY_SIMPLEX
        # search for yellow
        mask = cv2.inRange(HSV, lower_yellow, upper_yellow)
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4,iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        ret, binary = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY)
        _, contours_yellow, other = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_yellow = 0

        # search for red
        mask = cv2.inRange(HSV, lower_red, upper_red)
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4,iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        ret, binary = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY)
        _, contours_red, other = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_red = 0

        # search for blue        size9=[]

        mask = cv2.inRange(HSV, lower_blue, upper_blue)
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4,iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        ret, binary = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY)
        _, contours_blue, other = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_blue = 0


        # search for green
        mask = cv2.inRange(HSV, lower_green, upper_green)
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4,iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        ret, binary = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY)
        _, contours_green, other = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_green = 0


        # search for orange
        mask = cv2.inRange(HSV, lower_orange, upper_orange)
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4,iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        ret, binary = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY)
        _, contours_orange, other = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_orange = 0


        # search for white
        mask = cv2.inRange(HSV, lower_white, upper_white)
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4,iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        ret, binary = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY)
        _, contours_white, other = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_white = 0

        #    if i.size < 800:
        #        pass
        #    else:
        #        x, y, w, h = cv2.boundingRect(i)
        #        cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
        #        coord_x = int(0.5*(2*x+w))
        #        coord_y = int(0.5*(2*y+h))
        #        temp = [coo1rd_x, coord_y]
        #        coord_white.append(temp)
        #        cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
        #        cv2.putText(Img, str(num_white), (x-10, y-10), font, 1, (0, 0, 0), 2)
        #        total_coord.append(temp)
        #        num_white += 1
        # count and check if all nine node is found
        total = num_white + num_yellow + num_blue + num_green + num_orange + num_red
        total_contour = contours_red + contours_blue + contours_green +contours_orange + contours_white +contours_yellow
        if total >9:
            thread, thread1 = find9(total_contour)
        else:
            thread =0
            thread1 = 1000

        res_contuore = []
        for i in contours_white:
            if i.size < thread or i.size >= thread1:
                pass
            else:
                res_contuore.append(i)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
                coord_x = int(0.5*(2*x+w))
                coord_y = int(0.5*(2*y+h))
                temp = [coord_x, coord_y]
                coord_white.append(temp)
                cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
                cv2.putText(Img, str(num_white), (x-10, y-10), font, 1, (0, 0, 0), 2)
                total_coord.append(temp)
                num_white += 1
        #cv2.imshow('0',Img)
        #cv2.waitKey(0)
        for i in contours_yellow:
            if i.size < thread or i.size >= thread1:
                pass
            else:
                res_contuore.append(i)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
                coord_x = int(0.5*(2*x+w))
                coord_y = int(0.5*(2*y+h))
                temp = [coord_x, coord_y]
                coord_yellow.append(temp)
                cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
                cv2.putText(Img, str(num_yellow), (x-10, y-10), font, 1, (0, 0, 0), 2)
                total_coord.append(temp)
                num_yellow += 1

        for i in contours_red:
            if i.size < thread or i.size >= thread1:
                pass
            else:
                res_contuore.append(i)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
                coord_x = int(0.5*(2*x+w))
                coord_y = int(0.5*(2*y+h))
                temp = [coord_x, coord_y]
                coord_red.append(temp)
                cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
                cv2.putText(Img, str(num_red), (x-10, y-10), font, 1, (0, 0, 0), 2)
                total_coord.append(temp)
                num_red += 1

        for i in contours_blue:
            if i.size < thread or i.size >= thread1:
                pass
            else:
                res_contuore.append(i)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
                coord_x = int(0.5*(2*x+w))
                coord_y = int(0.5*(2*y+h))
                temp = [coord_x, coord_y]
                coord_blue.append(temp)
                cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
                cv2.putText(Img, str(num_blue), (x-10, y-10), font, 1, (0, 0, 0), 2)
                total_coord.append(temp)
                num_blue += 1

        for i in contours_orange:
            if i.size < thread or i.size >= thread1:
                pass
            else:
                res_contuore.append(i)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
                coord_x = int(0.5*(2*x+w))
                coord_y = int(0.5*(2*y+h))
                temp = [coord_x, coord_y]
                coord_orange.append(temp)
                cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
                cv2.putText(Img, str(num_orange), (x-10, y-10), font, 1, (0, 0, 0), 2)
                total_coord.append(temp)
                num_orange += 1

        for i in contours_green:
            if i.size < thread or i.size >= thread1:
                pass
            else:
                res_contuore.append(i)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Img, (x,y), (x+w, y+h), (0, 0, 0), 3)
                coord_x = int(0.5*(2*x+w))
                coord_y = int(0.5*(2*y+h))
                temp = [coord_x, coord_y]
                coord_green.append(temp)
                cv2.rectangle(Img, (coord_x-1, coord_y-1), (coord_x+1, coord_y+1), (0, 0, 0), 3)
                cv2.putText(Img, str(num_green), (x-10, y-10), font, 1, (0, 0, 0), 2)
                total_coord.append(temp)
                num_green += 1
        total = num_yellow + num_red + num_orange + num_green + num_blue + num_white
        RGB9 = []



        if total == 9:
            # sort coordinates
            sorted_coord = sortcoord(total_coord)
            # give value to index_color and idx_color

            def find_list(input_list, target):
                feedback = False
                for i in input_list:
                    if input_list[i][1] == target[1]:
                        if input_list[i][2] == target[2]:
                            feedback = True
                            break

        #    for i in sorted_coord:
        #        x = i[0]
        #        y = i[1]
        #        RGB9.append([HSV[y, x][0], HSV[y, x][1], HSV[y, x][2]])
        #    print RGB9
        #    for i in RGB9:
        #        print i
        #        if lower_red[0] <= i[0] <= upper_red[0] and lower_red[1] <= i[1] <= upper_red[1] and lower_red[2] <= i[2] <= upper_red[2]:
        #            print "red", i

            for i in range(len(sorted_coord)):
                try:
                    if coord_yellow.index(sorted_coord[i]) != None:
                        index_color[i] = "yellow"
                        idx_yellow.append(i)
                        continue
                except ValueError:
                    pass

                try:
                    if coord_green.index(sorted_coord[i]) != None:
                        index_color[i] = 'green'
                        idx_green.append(i)
                        continue
                except ValueError:
                    pass

                try:
                    if coord_orange.index(sorted_coord[i]) != None:
                        index_color[i] = 'orange'
                        idx_orange.append(i)
                        continue
                except ValueError:
                    pass

                try:
                    if coord_blue.index(sorted_coord[i]) != None:
                        index_color[i] = 'blue'
                        idx_blue.append(i)
                        continue
                except ValueError:
                    pass

                try:
                    if coord_red.index(sorted_coord[i]) != None:
                        index_color[i] = 'red'
                        idx_red.append(i)
                        continue
                except ValueError:
                    pass

                try:
                    if coord_white.index(sorted_coord[i]) != None:
                        index_color[i] = 'white'
                        idx_white.append(i)
                except ValueError:
                    pass

            print index_color
            print "the number of yellow is:", num_yellow, "with coordinates", coord_yellow, 'with index:', idx_yellow
            print "the number of red is:", num_red, "with coordinates", coord_red, 'with index:', idx_red
            print "the number of blue is:", num_blue, "with coordinates", coord_blue, 'with index:', idx_blue
            print "the number of green is:", num_green, "with coordinates", coord_green, 'with index:', idx_green
            print "the number of orange is:", num_orange, "with coordinates", coord_orange, 'with index:', idx_orange
            print "the number of white is:", num_white, "with coordinates", coord_white, 'with index:', idx_white
            print index_color[0:3]
            print index_color[3:6]
            print index_color[6:9]

            print sorted_coord
            cv2.imshow("1", Img)
            K= cv2.waitKey(0)
        else:
            print "Error!!!"
            print total
            cv2.imshow("1", Img)
            K = cv2.waitKey(0)
	return 0
img_path = 'pside5.jpg'
rec(img_path)


