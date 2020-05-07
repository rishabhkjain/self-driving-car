#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time
import os 
os.environ['GPIOZERO_PIN_FACTORY'] = os.environ.get('GPIOZERO_PIN_FACTORY', 'mock')
from gpiozero import LED
forwardPin = 17
backwardPin = 22
leftPin   = 6
rightPin = 19


forward = LED(forwardPin)
backward = LED(backwardPin)
left = LED(leftPin)
right = LED(rightPin)


def moveForward():
    backward.on()
    left.on()
    right.on()
    forward.off()

def moveBackward():
    forward.on()
    left.on()
    right.on()
    backward.off()

def moveLeft():
    backward.on()
    forward.on()
    right.on()
    left.off()

def moveRight():
    backward.on()
    left.on()
    forward.on()
    right.off()

def resetMove():
    backward.on()
    left.on()
    forward.on()
    right.on()


def callback(data):
    if (data.linear.x == 1):
        print("Going Forward")
        moveForward()
    elif (data.linear.x == -1):
        print("Going Backward")
        moveBackward()
    elif (data.angular.z == 1):
        print("Going Left")
        moveLeft()
    elif (data.angular.z == -1):
        print("Going Right")
        moveRight()
    else:
        print("Not Going")
        resetMove()
    

def listener():

    rospy.init_node('rc_controller', anonymous=True)
    resetMove()

    rospy.Subscriber('cmd_vel', Twist, callback)
    print("Initiated Controller\n")
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
