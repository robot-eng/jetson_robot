#!/usr/bin/env python
import sys, tty, termios, os, readchar
from geometry_msgs.msg import Twist
#import BTS7960 as #HBridge
import rospy

speedleft = 0
speedright = 0
print("w/s: forward/back")
print("a/d: left/right")
print("q: stoppt Motor")
print("x: Programm end")

def getch():
   ch = readchar.readchar()
   return ch
def printscreen():
   print("========== MotorSet ==========")
   print ("Motor Speedleft:  ", speedleft)
   print ("Motor Speedright: ", speedright)

if __name__ == '__main__':
   pub = rospy.Publisher('cmd_vel', Twist, queue_size=0)
   rospy.init_node('Control_motor', anonymous=True)
   #rospy.Subscriber('Control', String, queue_size=10)
   speed = Twist()

   while not rospy.is_shutdown():

      char = getch()
      if(char == "w"):

         speedleft = speedleft + 0.1
         speedright = speedright + 0.1

         if speedleft > 1:
            speedleft = 1
         if speedright > 1:
            speedright = 1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()
         
      if(char == "s"):

         speedleft = speedleft - 0.1
         speedright = speedright - 0.1

         if speedleft < -1:
            speedleft = -1
         if speedright < -1:
            speedright = -1
      
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "q"):
         speedleft = 0
         speedright = 0
         ##HBridge.setMotorLeft(0)
         ##HBridge.setMotorRight(0)
         printscreen()

      if(char == "d"):      
         speedright = speedright - 0.1
         speedleft = speedleft + 0.1
      
         if speedright < -1:
            speedright = -1
      
         if speedleft > 1:
            speedleft = 1
      
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "a"):
         speedleft = speedleft - 0.1
         speedright = speedright + 0.1
         
         if speedleft < -1:
            speedleft = -1
      
         if speedright > 1:
            speedright = 1
      
         #HBridge.setMotorLeft(speedleft)
         #HBridge.setMotorRight(speedright)
      
         printscreen()

      if(char == "x"):
         speedleft = 0
         speedright = 0
         print ("Program Ended motorset 0")
         rospy.loginfo_once("ctrl+c exit")
         break

      speed.linear.x = speedleft
      speed.linear.y = speedright
 
      char = ""
      
      pub.publish(speed)
