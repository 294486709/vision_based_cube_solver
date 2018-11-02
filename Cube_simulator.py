import copy
r = 'r'
o = 'o'
w = 'w'
y = 'y'
b = 'b'
g = 'g'

def display(red, orange, white, yellow, blue, green,*refrence):
    if len(refrence) != 0:
        color = refrence[0]
    else:
        color = str(input("Input refrence color:"))
    red_neighbor = [white,yellow,green,blue,orange,'white','yellow','green','blue','orange']
    blue_neighbor = [white,yellow,red,orange,green,'white','yellow','red','orange','green']
    orange_neighbor = [white,yellow,blue,green,red,'white','yellow','blue','green','red']
    green_neighbor = [white,yellow,orange,red,blue,'white','yellow','orange','red','blue']
    white_neighbor = [orange,red,green,blue,yellow,'orange','red','green','blue','yellow']
    yellow_neighbor = [red,orange,green,blue,white,'red','orange','green','blue','white']
    try:
        if color == 'r':
            temp = red_neighbor
            me = "red"
            print("                       ", temp[5])
            print("                  ", temp[0][0:3])
            print("                  ", temp[0][3:6])
            print("                  ", temp[0][6:9])
            print("    ", str(temp[7]), "             ", me, "              ", str(temp[8]), "            ", str(temp[9]))
            print(temp[2][0:3], "  ", red[0:3], "  ", temp[3][0:3], "  ", temp[4][0:3])
            print(temp[2][3:6], "  ", red[3:6], "  ", temp[3][3:6], "  ", temp[4][3:6])
            print(temp[2][6:9], "  ", red[6:9], "  ", temp[3][6:9], "  ", temp[4][6:9])
            print("                       ", str(temp[6]))
            print("                  ", temp[1][0:3])
            print("                  ", temp[1][3:6])
            print("                  ", temp[1][6:9])
            return True
        elif color == "g":
            temp = green_neighbor
            me = "green"
            up_1 = [temp[0][2],temp[0][5],temp[0][8]]
            up_2 = [temp[0][1],temp[0][4],temp[0][7]]
            up_3 = [temp[0][0],temp[0][3],temp[0][6]]
            down_1 = [temp[1][6],temp[1][3],temp[1][0]]
            down_2 = [temp[1][7],temp[1][4],temp[1][1]]
            down_3 = [temp[1][8],temp[1][5],temp[1][2]]

            print("                       ", temp[5])
            print("                  ", up_1)
            print("                  ", up_2)
            print("                  ", up_3)
            print("    ", str(temp[7]), "             ", me, "              ", str(temp[8]), "            ", str(temp[9]))
            print(temp[2][0:3], "  ", green[0:3], "  ", temp[3][0:3], "  ", temp[4][0:3])
            print(temp[2][3:6], "  ", green[3:6], "  ", temp[3][3:6], "  ", temp[4][3:6])
            print(temp[2][6:9], "  ", green[6:9], "  ", temp[3][6:9], "  ", temp[4][6:9])
            print("                       ", str(temp[6]))
            print("                  ", down_1)
            print("                  ", down_2)
            print("                  ", down_3)
            return True
        elif color == "o":
            temp = orange_neighbor
            me = "orange"
            up_1 = [temp[0][8],temp[0][7],temp[0][6]]
            up_2 = [temp[0][5],temp[0][4],temp[0][3]]
            up_3 = [temp[0][2],temp[0][1],temp[0][0]]
            down_1 = [temp[1][8],temp[1][7],temp[1][6]]
            down_2 = [temp[1][5],temp[1][4],temp[1][3]]
            down_3 = [temp[1][2],temp[1][1],temp[1][0]]
            print("                       ", temp[5])
            print("                  ", up_1)
            print("                  ", up_2)
            print("                  ", up_3)
            print("    ", str(temp[7]), "             ", me, "              ", str(temp[8]), "            ", str(temp[9]))
            print(temp[2][0:3], "  ", orange[0:3], "  ", temp[3][0:3], "  ", temp[4][0:3])
            print(temp[2][3:6], "  ", orange[3:6], "  ", temp[3][3:6], "  ", temp[4][3:6])
            print(temp[2][6:9], "  ", orange[6:9], "  ", temp[3][6:9], "  ", temp[4][6:9])
            print("                       ", str(temp[6]))
            print("                  ", down_1)
            print("                  ", down_2)
            print("                  ", down_3)
            return True
        elif color == "b":
            temp = blue_neighbor
            me = "blue"
            up_1 = [temp[0][6],temp[0][3],temp[0][0]]
            up_2 = [temp[0][7],temp[0][4],temp[0][1]]
            up_3 = [temp[0][8],temp[0][5],temp[0][2]]
            down_1 = [temp[1][2],temp[1][5],temp[1][8]]
            down_2 = [temp[1][1],temp[1][4],temp[1][7]]
            down_3 = [temp[1][0],temp[1][3],temp[1][6]]
            print("                       ", temp[5])
            print("                  ", up_1)
            print("                  ", up_2)
            print("                  ", up_3)
            print("    ", str(temp[7]), "             ", me, "              ", str(temp[8]), "            ", str(temp[9]))
            print(temp[2][0:3], "  ", blue[0:3], "  ", temp[3][0:3], "  ", temp[4][0:3])
            print(temp[2][3:6], "  ", blue[3:6], "  ", temp[3][3:6], "  ", temp[4][3:6])
            print(temp[2][6:9], "  ", blue[6:9], "  ", temp[3][6:9], "  ", temp[4][6:9])
            print("                       ", str(temp[6]))
            print("                  ", down_1)
            print("                  ", down_2)
            print("                  ", down_3)
            return True
        elif color == "w":
            temp = white_neighbor
            me = "white"
            up_1 = [temp[0][8],temp[0][7],temp[0][6]]
            up_2 = [temp[0][5],temp[0][4],temp[0][3]]
            up_3 = [temp[0][2],temp[0][1],temp[0][0]]
            left_1 = [temp[2][6],temp[2][3],temp[2][0]]
            left_2 = [temp[2][7],temp[2][4],temp[2][1]]
            left_3 = [temp[2][8],temp[2][5],temp[2][2]]
            right_1 = [temp[3][2],temp[3][5],temp[3][8]]
            right_2 = [temp[3][1],temp[3][4],temp[3][7]]
            right_3 = [temp[3][0],temp[3][3],temp[3][6]]
            back_1 = [temp[4][8],temp[4][7],temp[4][6]]
            back_2 = [temp[4][5],temp[4][4],temp[4][3]]
            back_3 = [temp[4][2],temp[4][1],temp[4][0]]
            print("                       ", temp[5])
            print("                  ", up_1)
            print("                  ", up_2)
            print("                  ", up_3)
            print("    ", str(temp[7]), "             ", me, "              ", str(temp[8]), "            ", str(temp[9]))
            print(left_1, "  ", white[0:3], "  ", right_1, "  ", back_1)
            print(left_2, "  ", white[3:6], "  ", right_2, "  ", back_2)
            print(left_3, "  ", white[6:9], "  ", right_3, "  ", back_3)
            print("                       ", str(temp[6]))
            print("                  ", temp[1][0:3])
            print("                  ", temp[1][3:6])
            print("                  ", temp[1][6:9])
            return True
        elif color == "y":
            temp = yellow_neighbor
            me = "yellow"
            left_1 = [temp[2][2],temp[2][5],temp[2][8]]
            left_2 = [temp[2][1],temp[2][4],temp[2][7]]
            left_3 = [temp[2][0],temp[2][3],temp[2][6]]
            right_1 = [temp[3][6],temp[3][3],temp[3][0]]
            right_2 = [temp[3][7],temp[3][4],temp[3][1]]
            right_3 = [temp[3][8],temp[3][5],temp[3][2]]
            back_1 = [temp[4][8],temp[4][7],temp[4][6]]
            back_2 = [temp[4][5],temp[4][4],temp[4][3]]
            back_3 = [temp[4][2],temp[4][1],temp[4][0]]
            down_1 = [temp[1][8],temp[1][7],temp[1][6]]
            down_2 = [temp[1][5],temp[1][4],temp[1][3]]
            down_3 = [temp[1][2],temp[1][1],temp[1][0]]
            print("                       ", temp[5])
            print("                  ", temp[0][0:3])
            print("                  ", temp[0][3:6])
            print("                  ", temp[0][6:9])
            print("    ", str(temp[7]), "             ", me, "              ", str(temp[8]), "            ", str(temp[9]))
            print(left_1, "  ", yellow[0:3], "  ", right_1, "  ", back_1)
            print(left_2, "  ", yellow[3:6], "  ", right_2, "  ", back_2)
            print(left_3, "  ", yellow[6:9], "  ", right_3, "  ", back_3)
            print("                       ", str(temp[6]))
            print("                  ", down_1)
            print("                  ", down_2)
            print("                  ", down_3)
            return True
    except NameError:
        print("Input Error")
        return False

def trans(red, orange, white, yellow, blue, green, refrence, dir):
    red_neighbor = [white,yellow,green,blue,orange,'white','yellow','green','blue','orange']
    blue_neighbor = [white,yellow,red,orange,green,'white','yellow','red','orange','green']
    orange_neighbor = [white,yellow,blue,green,red,'white','yellow','blue','green','red']
    green_neighbor = [white,yellow,orange,red,blue,'white','yellow','orange','red,blue']
    white_neighbor = [orange,red,green,blue,yellow,'orange','red,green','blue','yellow']
    yellow_neighbor = [red,orange,green,blue,white,'red','orange','green','blue','white']
    if refrence == "r":
        leftc = [green[2],green[5],green[8]]
        temp = copy.copy(red)
        neighbor = red_neighbor
        me=red
        if dir == 1:

            neighbor[2][2]=neighbor[1][0]
            neighbor[2][5]=neighbor[1][1]
            neighbor[2][8]=neighbor[1][2]
            neighbor[1][0]=neighbor[3][6]
            neighbor[1][1]=neighbor[3][3]
            neighbor[1][2]=neighbor[3][0]
            neighbor[3][0]=neighbor[0][6]
            neighbor[3][3]=neighbor[0][7]
            neighbor[3][6]=neighbor[0][8]
            neighbor[0][6]=leftc[2]
            neighbor[0][7]=leftc[1]
            neighbor[0][8]=leftc[0]
            me[0]=temp[6]
            me[1]=temp[3]
            me[2]=temp[0]
            me[3]=temp[7]
            me[5]=temp[1]
            me[6]=temp[8]
            me[7]=temp[5]
            me[8]=temp[2]
        elif dir == -1:
            me[0]=temp[2]
            me[1]=temp[5]
            me[2]=temp[8]
            me[3]=temp[1]
            me[5]=temp[7]
            me[6]=temp[0]
            me[7]=temp[3]
            me[8]=temp[6]
            neighbor[2][2]=neighbor[0][8]
            neighbor[2][5]=neighbor[0][7]
            neighbor[2][8]=neighbor[0][6]
            neighbor[0][6]=neighbor[3][0]
            neighbor[0][7]=neighbor[3][3]
            neighbor[0][8]=neighbor[3][6]
            neighbor[3][0]=neighbor[1][2]
            neighbor[3][3]=neighbor[1][1]
            neighbor[3][6]=neighbor[1][0]
            neighbor[1][0]=leftc[0]
            neighbor[1][1]=leftc[1]
            neighbor[1][2]=leftc[2]

    elif refrence == "g":
        leftc = [orange[2],orange[5],orange[8]]
        temp = copy.copy(green)
        neighbor = green_neighbor
        me=green
        if dir == 1:

            neighbor[2][2]=neighbor[1][6]
            neighbor[2][5]=neighbor[1][3]
            neighbor[2][8]=neighbor[1][0]
            neighbor[1][0]=neighbor[3][0]
            neighbor[1][3]=neighbor[3][3]
            neighbor[1][6]=neighbor[3][6]
            neighbor[3][0]=neighbor[0][0]
            neighbor[3][3]=neighbor[0][3]
            neighbor[3][6]=neighbor[0][6]
            neighbor[0][0]=leftc[2]
            neighbor[0][3]=leftc[1]
            neighbor[0][6]=leftc[0]
            me[0]=temp[6]
            me[1]=temp[3]
            me[2]=temp[0]
            me[3]=temp[7]
            me[5]=temp[1]
            me[6]=temp[8]
            me[7]=temp[5]
            me[8]=temp[2]
        elif dir == -1:
            me[0]=temp[2]
            me[1]=temp[5]
            me[2]=temp[8]
            me[3]=temp[1]
            me[5]=temp[7]
            me[6]=temp[0]
            me[7]=temp[3]
            me[8]=temp[6]
            neighbor[2][2]=neighbor[0][6]
            neighbor[2][5]=neighbor[0][3]
            neighbor[2][8]=neighbor[0][0]
            neighbor[0][0]=neighbor[3][0]
            neighbor[0][3]=neighbor[3][3]
            neighbor[0][6]=neighbor[3][6]
            neighbor[3][0]=neighbor[1][0]
            neighbor[3][3]=neighbor[1][3]
            neighbor[3][6]=neighbor[1][6]
            neighbor[1][0]=leftc[2]
            neighbor[1][3]=leftc[1]
            neighbor[1][6]=leftc[0]
    elif refrence == "b":
        leftc = [red[2],red[5],red[8]]
        temp = copy.copy(blue)
        neighbor = blue_neighbor
        me=blue
        if dir == 1:

            neighbor[2][2]=neighbor[1][2]
            neighbor[2][5]=neighbor[1][5]
            neighbor[2][8]=neighbor[1][8]
            neighbor[1][2]=neighbor[3][6]
            neighbor[1][5]=neighbor[3][3]
            neighbor[1][8]=neighbor[3][0]
            neighbor[3][0]=neighbor[0][8]
            neighbor[3][3]=neighbor[0][5]
            neighbor[3][6]=neighbor[0][2]
            neighbor[0][2]=leftc[0]
            neighbor[0][5]=leftc[1]
            neighbor[0][8]=leftc[2]
            me[0]=temp[6]
            me[1]=temp[3]
            me[2]=temp[0]
            me[3]=temp[7]
            me[5]=temp[1]
            me[6]=temp[8]
            me[7]=temp[5]
            me[8]=temp[2]
        elif dir == -1:
            me[0]=temp[2]
            me[1]=temp[5]
            me[2]=temp[8]
            me[3]=temp[1]
            me[5]=temp[7]
            me[6]=temp[0]
            me[7]=temp[3]
            me[8]=temp[6]
            neighbor[2][2]=neighbor[0][2]
            neighbor[2][5]=neighbor[0][5]
            neighbor[2][8]=neighbor[0][8]
            neighbor[0][2]=neighbor[3][6]
            neighbor[0][5]=neighbor[3][3]
            neighbor[0][8]=neighbor[3][0]
            neighbor[3][0]=neighbor[1][8]
            neighbor[3][3]=neighbor[1][5]
            neighbor[3][6]=neighbor[1][2]
            neighbor[1][2]=leftc[1]
            neighbor[1][5]=leftc[1]
            neighbor[1][8]=leftc[2]

    elif refrence == "o":
        leftc = [blue[2],blue[5],blue[8]]
        temp = copy.copy(orange)
        neighbor = orange_neighbor
        me=orange
        if dir == 1:

            neighbor[2][2]=neighbor[1][8]
            neighbor[2][5]=neighbor[1][7]
            neighbor[2][8]=neighbor[1][6]
            neighbor[1][6]=neighbor[3][0]
            neighbor[1][7]=neighbor[3][3]
            neighbor[1][8]=neighbor[3][6]
            neighbor[3][0]=neighbor[0][2]
            neighbor[3][3]=neighbor[0][1]
            neighbor[3][6]=neighbor[0][0]
            neighbor[0][0]=leftc[0]
            neighbor[0][1]=leftc[1]
            neighbor[0][2]=leftc[2]
            me[0]=temp[6]
            me[1]=temp[3]
            me[2]=temp[0]
            me[3]=temp[7]
            me[5]=temp[1]
            me[6]=temp[8]
            me[7]=temp[5]
            me[8]=temp[2]
        elif dir == -1:
            me[0]=temp[2]
            me[1]=temp[5]
            me[2]=temp[8]
            me[3]=temp[1]
            me[5]=temp[7]
            me[6]=temp[0]
            me[7]=temp[3]
            me[8]=temp[6]
            neighbor[2][2]=neighbor[0][0]
            neighbor[2][5]=neighbor[0][1]
            neighbor[2][8]=neighbor[0][2]
            neighbor[0][0]=neighbor[3][6]
            neighbor[0][1]=neighbor[3][3]
            neighbor[0][2]=neighbor[3][0]
            neighbor[3][0]=neighbor[1][6]
            neighbor[3][3]=neighbor[1][7]
            neighbor[3][6]=neighbor[1][8]
            neighbor[1][6]=leftc[2]
            neighbor[1][7]=leftc[1]
            neighbor[1][8]=leftc[0]


    elif refrence == "w":
        leftc = [green[0],green[1],green[2]]
        temp = copy.copy(white)
        neighbor = white_neighbor
        me=white
        if dir == 1:

            neighbor[2][0]=neighbor[1][0]
            neighbor[2][1]=neighbor[1][1]
            neighbor[2][2]=neighbor[1][2]
            neighbor[1][0]=neighbor[3][0]
            neighbor[1][1]=neighbor[3][1]
            neighbor[1][2]=neighbor[3][2]
            neighbor[3][0]=neighbor[0][0]
            neighbor[3][1]=neighbor[0][1]
            neighbor[3][2]=neighbor[0][2]
            neighbor[0][0]=leftc[0]
            neighbor[0][1]=leftc[1]
            neighbor[0][2]=leftc[2]
            me[0]=temp[6]
            me[1]=temp[3]
            me[2]=temp[0]
            me[3]=temp[7]
            me[5]=temp[1]
            me[6]=temp[8]
            me[7]=temp[5]
            me[8]=temp[2]
        elif dir == -1:
            me[0]=temp[2]
            me[1]=temp[5]
            me[2]=temp[8]
            me[3]=temp[1]
            me[5]=temp[7]
            me[6]=temp[0]
            me[7]=temp[3]
            me[8]=temp[6]
            neighbor[2][0]=neighbor[0][0]
            neighbor[2][1]=neighbor[0][1]
            neighbor[2][2]=neighbor[0][2]
            neighbor[0][0]=neighbor[3][0]
            neighbor[0][1]=neighbor[3][1]
            neighbor[0][2]=neighbor[3][2]
            neighbor[3][0]=neighbor[1][0]
            neighbor[3][1]=neighbor[1][1]
            neighbor[3][2]=neighbor[1][2]
            neighbor[1][0]=leftc[0]
            neighbor[1][1]=leftc[1]
            neighbor[1][2]=leftc[2]

    elif refrence == "y":
        leftc = [green[8],green[7],green[6]]
        temp = copy.copy(yellow)
        neighbor = yellow_neighbor
        me=yellow
        if dir == 1:

            neighbor[2][8]=neighbor[1][8]
            neighbor[2][7]=neighbor[1][7]
            neighbor[2][6]=neighbor[1][6]
            neighbor[1][8]=neighbor[3][8]
            neighbor[1][7]=neighbor[3][7]
            neighbor[1][6]=neighbor[3][6]
            neighbor[3][8]=neighbor[0][8]
            neighbor[3][7]=neighbor[0][7]
            neighbor[3][6]=neighbor[0][6]
            neighbor[0][8]=leftc[0]
            neighbor[0][7]=leftc[1]
            neighbor[0][6]=leftc[2]
            me[0]=temp[6]
            me[1]=temp[3]
            me[2]=temp[0]
            me[3]=temp[7]
            me[5]=temp[1]
            me[6]=temp[8]
            me[7]=temp[5]
            me[8]=temp[2]
        elif dir == -1:
            me[0]=temp[2]
            me[1]=temp[5]
            me[2]=temp[8]
            me[3]=temp[1]
            me[5]=temp[7]
            me[6]=temp[0]
            me[7]=temp[3]
            me[8]=temp[6]
            neighbor[2][8]=neighbor[0][8]
            neighbor[2][7]=neighbor[0][7]
            neighbor[2][6]=neighbor[0][6]
            neighbor[0][8]=neighbor[3][8]
            neighbor[0][7]=neighbor[3][7]
            neighbor[0][6]=neighbor[3][6]
            neighbor[3][8]=neighbor[1][8]
            neighbor[3][7]=neighbor[1][7]
            neighbor[3][6]=neighbor[1][6]
            neighbor[1][8]=leftc[0]
            neighbor[1][7]=leftc[1]
            neighbor[1][6]=leftc[2]
    print(refrence, dir)

    while 1:
        k = display(red, orange, white, yellow, blue, green, w)
        if k == True:
            break




    return red, orange, white, yellow, blue, green

def main_disp(red,orange,white,yellow,blue,green):
    if 1 == 1:
        # displace initial
        while 1:
            k = display(red, orange, white, yellow, blue, green,"y")
            if k == True:
                break
        while 1:
            list1 = input("Please input a refrence:")
            list2 = int(input("please inout a direction:"))
            #list1 = [r,o,w,y,b,g,g,b,y,w,o,r]
            #list2 = [1,1,1,1,1,1,-1,-1,-1,-1,-1,-1]
            for i in range(len(list1)):
                red, orange, white, yellow, blue, green = trans(red, orange, white, yellow, blue, green, list1[i], list2[i])
            k =display(red, orange, white, yellow, blue, green)
            if k == True:
                break
    return red,orange,white,yellow,blue,green


    for i in range(len(solver_direction)):
        print(solver_direction[i],solver_refrence[i])
    return red,orange,white,yellow,blue,green


