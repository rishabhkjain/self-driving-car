#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time
import os 

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

forwardPin = 17
backwardPin = 22
leftPin   = 6
rightPin = 19

GPIO.setup(rightPin, GPIO.OUT)
GPIO.output(rightPin, GPIO.HIGH)
GPIO.setup(leftPin, GPIO.OUT)
GPIO.output(leftPin, GPIO.HIGH)
GPIO.setup(forwardPin, GPIO.OUT)
GPIO.output(forwardPin, GPIO.HIGH)
GPIO.setup(backwardPin, GPIO.OUT)
GPIO.output(backwardPin, GPIO.HIGH)



def moveForward():
    GPIO.output(backwardPin, GPIO.HIGH)
    GPIO.output(leftPin, GPIO.HIGH)
    GPIO.output(rightPin, GPIO.HIGH)
    GPIO.output(forwardPin, GPIO.LOW)

def moveBackward():
    GPIO.output(forwardPin, GPIO.HIGH)
    GPIO.output(leftPin, GPIO.HIGH)
    GPIO.output(rightPin, GPIO.HIGH)
    GPIO.output(backwardPin, GPIO.LOW)

def moveLeft():
    GPIO.output(backwardPin, GPIO.HIGH)
    GPIO.output(forwardPin, GPIO.HIGH)
    GPIO.output(rightPin, GPIO.HIGH)
    GPIO.output(leftPin, GPIO.LOW)

def moveRight():
    GPIO.output(backwardPin, GPIO.HIGH)
    GPIO.output(leftPin, GPIO.HIGH)
    GPIO.output(forwardPin, GPIO.HIGH)
    GPIO.output(rightPin, GPIO.LOW)

def resetMove():
    GPIO.output(backwardPin, GPIO.HIGH)
    GPIO.output(leftPin, GPIO.HIGH)
    GPIO.output(rightPin, GPIO.HIGH)
    GPIO.output(forwardPin, GPIO.HIGH)


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
