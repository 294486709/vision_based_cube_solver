import rospy
import baxter_interface

rospy.init_node('cube_solver')
left = baxter_interface.Limb('left')
right = baxter_interface.Limb('right')

anglesl = left.joint_angles()
anglesr = right.joint_angles()

fleft = open('Left.txt','a')
fright = open('Right.txt','a')



for value in anglesl.items():
    fleft.write(str(value[1]))
    fleft.write('\n')

for value in anglesr.items():
    fright.write(str(value[1]))
    fright.write('\n')
    

fleft.close()
fright.close()
