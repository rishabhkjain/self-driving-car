#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64, UInt8
    
    
throttlePub = rospy.Publisher('throttle_cmd', Float64, queue_size = 1)
gearPub = rospy.Publisher('gear_cmd', UInt8, queue_size=1)
steeringPub = rospy.Publisher('steering_cmd', Float64, queue_size=1)





def callback(data):
    backVal = data.axes[2]
    forwardVal = data.axes[5]
    leftButton = data.buttons[4]
    rightButton = data.buttons[5]
    steeringVal = Float64()
    if leftButton:
        steeringVal.data = (30)
        steeringPub.publish(steeringVal)
        print("Turning Left")
    elif rightButton:
        steeringVal.data = (-30)
        steeringPub.publish(steeringVal)
        print("Turning Right")
    else: 
        steeringVal.data = (0)
        steeringPub.publish(steeringVal)
        print("Straight")
    

    if forwardVal != 1.0: 
        gearVal = UInt8()
        gearVal.data = 0
        gearPub.publish(gearVal)
        throttleVal = Float64()
        throttleVal.data = (-forwardVal + 1)/2
        throttlePub.publish(throttleVal)
        print("Moving Forward")
    if backVal != 1.0:
        gearVal = UInt8()
        gearVal.data = 1
        gearPub.publish(gearVal)
        throttleVal = Float64()
        throttleVal.data = (-backVal + 1)/2
        throttlePub.publish(throttleVal)
        print("Moving Backward")
    return None

def listener():

    rospy.init_node('teleop_controller', anonymous=True)

    rospy.Subscriber('joy', Joy, callback)
    print("Initiated Controller\n")
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()