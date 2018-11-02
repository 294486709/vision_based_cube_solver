import rospy
import baxter_interface
import time

def main():
    rospy.init_node("HB")
    right = baxter_interface.Limb('right')
    left =  baxter_interface.Limb('left')
    right.set_joint_position_speed(0.1)
    left.set_joint_position_speed(0.8)
    wave_1 = {'right_s0': -0.459, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906,
              'right_w1': -1.545, 'right_w2': -0.276}
    wave_2 = {'right_s0': -0.395, 'right_s1': -0.202, 'right_e0': 1.831, 'right_e1': 1.981, 'right_w0': -1.979,
              'right_w1': -1.100, 'right_w2': -0.448}
    i=1
    while i < 10:
        print right.joint_velocities()
        right_stat = right.joint_velocities()
        if abs(right_stat['right_s0']) < 0.1 and abs(right_stat['right_s1']) < 0.1 and abs(right_stat['right_w0']) < 0.1 and abs(right_stat['right_w1']) < 0.1 and abs(right_stat['right_w2']) < 0.1 and abs(right_stat['right_e0']) < 0.1 and abs(right_stat['right_e1']) < 0.1:
            print 'stoped'
            if i % 2 == 1:
                print "set wave1"
                right.set_joint_position_speed(0.01)
                print "speed 0.1"
                right.move_to_joint_positions(wave_1)
                #time.sleep(1)
                print right.joint_velocities()
                i+=1
            else:
                print 'set wave2'
                right.set_joint_position_speed(0.8)
                print "speed 0.8"
                right.move_to_joint_positions(wave_2)
                #time.sleep(1)
                print right.joint_velocities()
                i+=1
        rospy.sleep(0.1)

main()