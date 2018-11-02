import rospy
import baxter_interface
import time as ti
import os


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


def grib(right_g,left,right):
    right_g.close()
    left_data, right_data = readfile('2_left.txt','2_right.txt')
    movement(left_data,right_data,left,right)
    print "Taking Photo of NO1 side"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    left_data, right_data = readfile('3_left.txt','3_right.txt')
    movement(left_data,right_data,left,right)
    print "Taking Photo of NO2 side"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    left_data, right_data = readfile('5_left.txt','5_right.txt')
    movement(left_data,right_data,left,right)
    print "Taking Photo of NO3 side"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    left_data, right_data = readfile('4_left.txt','4_right.txt')
    movement(left_data,right_data,left,right)
    ti.sleep(5)
    right_g.open()
    left_data, right_data = readfile('6_left.txt','6_right.txt')
    movement(left_data,right_data,left,right)
    left_data,right_data = readfile('empty.txt','rec01.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data,right_data = readfile('empty.txt','rec02.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('7_left.txt','7_right.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data, right_data = readfile('empty.txt','front01.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('empty.txt','front02.txt')
    movement(left_data,right_data,left,right)
    left_data,right_data = readfile('empty.txt','rec01.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data,right_data = readfile('empty.txt','rec02.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('7_left.txt','7_right.txt')
    movement(left_data,right_data,left,right)
    right_g.close()
    left_data, right_data = readfile('empty.txt','tofront01.txt')
    movement(left_data,right_data,left,right)
    right_g.open()
    left_data, right_data = readfile('empty.txt','tofront02.txt')
    movement(left_data,right_data,left,right)
    left_data, right_data = readfile('empty.txt', 'rec01.txt')
    movement(left_data, right_data, left, right)
    right_g.close()
    left_data, right_data = readfile('empty.txt', 'rec02.txt')
    movement(left_data, right_data, left, right)
    right_g.open()
    left_data, right_data = readfile('7_left.txt', '7_right.txt')
    movement(left_data, right_data, left, right)
    right_g.close()
    left_data, right_data = readfile('2_left.txt','2_right.txt')
    movement(left_data,right_data,left,right)
    print "Taking Photo of NO4 side"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    left_data, right_data = readfile('3_left.txt','3_right.txt')
    movement(left_data,right_data,left,right)
    print "Taking Photo of NO5 side"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    left_data, right_data = readfile('5_left.txt','5_right.txt')
    movement(left_data,right_data,left,right)
    print "Taking Photo of NO6 side"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    left_data, right_data = readfile('4_left.txt','4_right.txt')
    movement(left_data,right_data,left,right)
    ti.sleep(5)
    right_g.open()
    #left_data, right_data = readfile('5_left.txt','5_right.txt')
    #movement(left_data,right_data,left,right)


def main():
    rospy.init_node('cube_solver')
    left = baxter_interface.Limb('left')
    right = baxter_interface.Limb('right')
    left.move_to_neutral()
    right.move_to_neutral()
    right_g = baxter_interface.Gripper('right')
    right_g.calibrate()
    right_g.open()
    right_data = [0.803805932852,-0.671500089897,0.169888372258,0.736694273382,2.88004892925,-0.185995170531, 1.42084970478]
    right_move = {'right_s0': right_data[0], 'right_s1': right_data[1], 'right_w0': right_data[2],'right_w1': right_data[3], 'right_w2': right_data[4], 'right_e0': right_data[5],'right_e1': right_data[6]}
    right.move_to_joint_positions(right_move)
    print "Adjust table position"
    dd=os.system('read "Press any key to continue"')
    print "Pressed"
    right.set_joint_position_speed(0.3)
    left.set_joint_position_speed(0.3)
    path1 = 'init_left.txt'
    path2 = 'init_right.txt'
    left_data, right_data = readfile(path1,path2)
    movement(left_data,right_data,left,right)
    print "init complete"
    grib(right_g,left,right)
    #left.move_to_neutral()
    #right.move_to_neutral()


if __name__ == "__main__":
    main()
