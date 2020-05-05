#!/usr/bin/env python

import rospy
import serial 
from geometry_msgs.msg import Twist
import time

port = '/dev/ttyACM0'

#initiate arduino 
ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

def callback(data):
    ard.flush()
    if (data.linear.x == 1):
        print("Going Forward")
        command = 'w'
    elif (data.linear.x == -1):
        print("Going Backward")
        command = 's'
    elif (data.angular.z == 1):
        print("Going Left")
        command = 'a'
    elif (data.angular.z == -1):
        print("Going Right")
        command = 'd'
    else:
        print("Not Going")
        command = 'z'
    ard.write(command)
    time.sleep(0.5)
    

def listener():

    rospy.init_node('rc_controller', anonymous=True)

    rospy.Subscriber('cmd_vel', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
