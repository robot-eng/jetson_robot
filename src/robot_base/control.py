#!/usr/bin/env python
import sys, tty, termios, os, readchar
from geometry_msgs.msg import Twist
#import BTS7960 as #HBridge
import rospy

speedleftfront = 0
speedleftback = 0
speedrightfront = 0
speedrightback = 0
print("w/s: forward/back")
print("a/d: left/right")
print("q: stoppt Motor")
print("x: Programm end")

def getch():
   ch = readchar.readchar()
   return ch
def printscreen():
   print("========== MotorSet ==========")
   print ("Motor speedleftfront:  ", speedleftfront)
   print ("Motor speedleftback: ", speedleftback)
   print ("Motor speedleftfront:  ", speedrightfront)
   print ("Motor speedleftback: ", speedrightback)
   
if __name__ == '__main__':
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=0)
    rospy.init_node('Control_motor', anonymous=True)
    #rospy.Subscriber('Control', String, queue_size=10)
    speed = Twist()

    while not rospy.is_shutdown():

        char = getch()
        if(char == "w"):

            speedleftfront = speedleftfront + 0.1
            speedleftback = speedleftback + 0.1
            speedrightfront = speedrightfront + 0.1
            speedrightback = speedrightback + 0.1

            if speedleftfront  > 1:
                speedleftfront  = 1
            if speedleftback > 1:
                speedleftback = 1
            if speedrightfront  > 1:
                speedrightfront  = 1
            if speedrightback > 1:
                speedrightback = 1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
            printscreen()
         
        if(char == "s"):

            speedleftfront = speedleftfront + 0.1
            speedleftback = speedleftback + 0.1
            speedrightfront = speedrightfront + 0.1
            speedrightback = speedrightback + 0.1

            if speedleftfront  < -1:
                speedleftfront  = -1
            if speedleftback < -1:
                speedleftback = -1
            if speedrightfront  < -1:
                speedrightfront  = -1
            if speedrightback < -1:
                speedrightback = -1
      
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
            printscreen()

        if(char == "q"):
            speedleftfront = 0
            speedleftback = 0
            speedrightfront = 0
            speedrightback = 0
         ##HBridge.setMotorLeft(0)
         ##HBridge.setMotorRight(0)
            printscreen()

        if(char == "d"):      
            speedrightfront = speedrightfront - 0.1
            speedrightback = speedrightback - 0.1
            speedleftfront = speedleftfront + 0.1
            speedleftback = speedleftback + 0.1
      
            if speedrightfront < -1:
                speedrightfront = -1
            if speedrightback < -1:
                speedrightback = -1
      
            if speedleftfront > 1:
                speedleftfront = 1
            if speedleftback > 1:
                speedleftback = 1
      
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
            printscreen()

        if(char == "a"):
            speedrightfront = speedrightfront + 0.1
            speedrightback = speedrightback + 0.1
            speedleftfront = speedleftfront - 0.1
            speedleftback = speedleftback - 0.1
      
            if speedrightfront > 1:
                speedrightfront = 1
            if speedrightback > 1:
                speedrightback = 1
      
            if speedleftfront < -1:
                speedleftfront = -1
            if speedleftback < -1:
                speedleftback = 1          
      
         #HBridge.setMotorLeft(speedleft)
         #HBridge.setMotorRight(speedright)
      
            printscreen()

        if(char == "x"):
            speedleftfront = 0
            speedleftback = 0
            speedrightfront = 0
            speedrightback = 0
            print ("Program Ended motorset 0")
            rospy.loginfo_once("ctrl+c exit")
            break

        speed.linear.x = speedleftfront
        speed.linear.y = speedleftback
        speed.linear.z = speedrightfront    
        speed.angular.x = speedrightback
        
        char = ""
      
        pub.publish(speed)