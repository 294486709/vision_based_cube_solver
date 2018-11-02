import baxter_interface
import rospy
import time as ti


def lr(left,right,right_g):
    right_g.open()
    left_data,right_data = readfile('empty.txt','filplr01.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data,right_data = readfile('empty.txt','filplr02.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data,right_data = readfile('empty.txt','filplr03.txt')
    movement(left_data,right_data,left,right)




def lr_i(left,right,right_g):
    right_g.open()
    left_data,right_data = readfile('empty.txt','filplr01.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data,right_data = readfile('empty.txt','filplr04.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data,right_data = readfile('empty.txt','filplr05.txt')
    movement(left_data,right_data,left,right)


def fr(left,right,right_g):
    right_g.open()
    left_data, right_data = readfile('7_left.txt','7_right.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data, right_data = readfile('empty.txt','tofront01.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('empty.txt','tofront02.txt')
    movement(left_data,right_data,left,right)


def fr_i(left,right,right_g):
    right_g.open()
    left_data, right_data = readfile('empty.txt','common1.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data, right_data = readfile('empty.txt','filplr06.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('empty.txt','077.txt')
    movement(left_data,right_data,left,right)


def hitwall_i(left,right,right_g):
    right_g.open()
    left_data, right_data = readfile('empty.txt','common1.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data, right_data = readfile('empty.txt','hitwall_i.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('empty.txt','LASTT.txt')
    movement(left_data,right_data,left,right)









def recov(left,right,right_g):
    right_g.open()
    left_data,right_data = readfile('empty.txt','rec01.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data,right_data = readfile('empty.txt','rec02.txt')
    movement(left_data,right_data,left,right)
    right_g.open()










def movement(left_data,right_data,left,right):
    left_empty = False
    right_empty = False
    ct = 1
    while 1:
        print 'loot NO.', ct
        left_free = False
        right_free = False
        if len(left_data) == 0:
            left_empty = True
            print 'left limb operation is completed'
        if len(right_data) == 0:
            right_empty = True
            print 'right limb operation is completed'
        print left_empty,right_empty
        if left_empty == True and right_empty == True:
            print "The list is empty"
            break
        elif left_empty == False and right_empty == False:
            left_move = {'left_w0': left_data[0], 'left_w1': left_data[1], 'left_w2': left_data[2], 'left_e0': left_data[3],'left_e1': left_data[4], 'left_s0': left_data[5], 'left_s1': left_data[6]}
            left.move_to_joint_positions(left_move)
            for j in range(7):
                del left_data[0]

            right_move = {'right_s0': right_data[0], 'right_s1': right_data[1], 'right_w0': right_data[2],'right_w1': right_data[3], 'right_w2': right_data[4], 'right_e0': right_data[5],'right_e1': right_data[6]}
            right.move_to_joint_positions(right_move)
            for j in range(7):
                del right_data[0]
        elif left_empty == True and right_empty == False:
            right_move = {'right_s0': right_data[0], 'right_s1': right_data[1], 'right_w0': right_data[2],'right_w1': right_data[3], 'right_w2': right_data[4], 'right_e0': right_data[5],'right_e1': right_data[6]}
            right.move_to_joint_positions(right_move)
            for j in range(7):
                del right_data[0]
        else:
            left_move = {'left_w0': left_data[0], 'left_w1': left_data[1], 'left_w2': left_data[2], 'left_e0': left_data[3],'left_e1': left_data[4], 'left_s0': left_data[5], 'left_s1': left_data[6]}
            left.move_to_joint_positions(left_move)
            for j in range(7):
                del left_data[0]
        ct += 1
        ti.sleep(0.5)


def readfile(path1,path2):
    fleft = open(path1,'r')
    fright = open(path2,'r')
    left_data = []
    right_data = []

    while 1:
        line1 = fleft.readline()
        line1 = line1.replace("\n","")
        if not line1:
            break
        else:
            left_data.append(float(line1))

    while 1:
        line1 = fright.readline()
        line1 = line1.replace("\n","")
        if not line1:
            break
        else:
            right_data.append(float(line1))

    return left_data,right_data


def main():
    rospy.init_node('cube_solrver')
    left = baxter_interface.Limb('left')
    right = baxter_interface.Limb('right')
    left.move_to_neutral()
    right.move_to_neutral()
    right_g = baxter_interface.Gripper('right')
    right_g.calibrate()
    right_g.open()
    f = open('instructions.txt', 'r')
    data = f.read()
    ins=[]
    tempp=[]

    for line in data:
        if line == '\n':
            pass
        elif line == '1':
            ins.append(tempp)
            tempp=[]
            continue
        else:
            tempp.append(line)
    inss = []
    for i in ins:
        temppp = []
        if len(i) == 1:
            direction = '+'
        else:
            direction = '-'
        if i[0] == 'r':
            face = 'front'
        elif i[0] == 'b':
            face = 'right'
        elif i[0] == 'g':
            face = 'left'
        elif i[0] == 'w':
            face = 'top'
        elif i[0] == 'o':
            face = 'back'
        elif i[0] == 'y':
            face = 'bottom'
        temppp.append(face)
        temppp.append(direction)
        inss.append(temppp)

    for i in range(len(ins)):
        currentface = inss[i][0]
        currentdirection = inss[i][1]
        print currentface,currentdirection
        if currentface == 'bottom':
            pass
        elif currentface == 'top':
            recov(left, right, right_g)
            fr(left,right,right_g)
            recov(left, right, right_g)
            fr(left,right,right_g)
        elif currentface == 'front':
            recov(left, right, right_g)
            fr_i(left,right,right_g)
        elif currentface == 'left':
            recov(left, right, right_g)
            lr_i(left,right,right_g)
            recov(left, right, right_g)
            fr_i(left,right,right_g)
        elif currentface == 'back':
            recov(left, right, right_g)
            fr(left,right,right_g)
        elif currentface == 'right':
            recov(left, right, right_g)
            lr(left,right,right_g)
            recov(left, right, right_g)
            fr_i(left,right,right_g)

        if currentdirection == '-':
            recov(left, right, right_g)
            hitwall_i(left, right, right_g)
        elif currentdirection == '+':
            recov(left, right, right_g)
            hitwall_i(left, right, right_g)
            recov(left, right, right_g)
            hitwall_i(left, right, right_g)
            recov(left, right, right_g)
            hitwall_i(left, right, right_g)

        if currentface == 'bottom':
            pass
        elif currentface == 'top':
            recov(left, right, right_g)
            fr_i(left,right,right_g)
            recov(left, right, right_g)
            fr_i(left,right,right_g)
        elif currentface == 'front':
            recov(left, right, right_g)
            fr(left,right,right_g)
        elif currentface == 'left':
            recov(left, right, right_g)
            fr(left,right,right_g)
            recov(left, right, right_g)
            lr(left,right,right_g)
        elif currentface == 'back':
            recov(left, right, right_g)
            fr_i(left,right,right_g)
        elif currentface == 'right':
            recov(left, right, right_g)
            fr(left,right,right_g)
            recov(left, right, right_g)
            lr_i(left,right,right_g)



if __name__ == '__main__':
    main()
