#!/usr/bin/env python
import sys, tty, termios, os, readchar
from geometry_msgs.msg import Twist
#import BTS7960 as #HBridge
import rospy

speedleft_f = 0
speedleft_b = 0
speedright_f = 0
speedright_b = 0
print("(w,W)/(s,S): forward/back")
print("(a,A)/(d,D): left/right")
print("(q,Q)/(e,E): <---- left/right ---->")
print("r/R: (/)forward , (/)back")
print("f/F: (\)forward , (\)back")
print("z/Z : stoppt Motor")
print("x/X : Programm end")

def getch():
   ch = readchar.readchar()
   return ch
def printscreen():
   print("========== MotorSet ==========")
   print ("Motor Speedleft:  ", speedleft_f)
   print ("Motor Speedright: ", speedleft_b)
   print ("Motor Speedleft:  ", speedright_f)
   print ("Motor Speedright: ", speedright_b)

if __name__ == '__main__':
   pub = rospy.Publisher('cmd_vel', Twist, queue_size=0)
   rospy.init_node('Control_motor', anonymous=True)
   #rospy.Subscriber('Control', String, queue_size=10)
   speed = Twist()

   while not rospy.is_shutdown():

      char = getch()
      if(char == "w" or char == "W"):

         speedleft_f = speedleft_f + 0.1
         speedleft_b = speedleft_b + 0.1
         speedright_f = speedright_f + 0.1
         speedright_b = speedright_b + 0.1

         if speedleft_f > 1:
            speedleft_f = 1
         if speedleft_b > 1:
            speedleft_b = 1
         if speedright_f > 1:
            speedright_f = 1
         if speedright_b > 1:
            speedright_b = 1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "r"):

         speedleft_f = speedleft_f + 0.01
         speedleft_b = speedleft_b + 0.1
         speedright_f = speedright_f + 0.1
         speedright_b = speedright_b + 0.01

         if speedleft_f >= 0.01:
            speedleft_f = 0.01
         if speedleft_b > 1:
            speedleft_b = 1
         if speedright_f > 1:
            speedright_f = 1
         if speedright_b >= 0.01:
            speedright_b = 0.01
            
         printscreen()

      if(char == "f"):

         speedleft_f = speedleft_f + 0.1
         speedleft_b = speedleft_b + 0.01
         speedright_f = speedright_f + 0.01
         speedright_b = speedright_b + 0.1

         if speedleft_f > 1:
            speedleft_f = 1
         if speedleft_b >= 0.01:
            speedleft_b = 0.01
         if speedright_f >= 0.01:
            speedright_f = 0.01
         if speedright_b > 1:
            speedright_b = 1
            
         printscreen()

      if(char == "F"):

         speedleft_f = speedleft_f - 0.1
         speedleft_b = speedleft_b + 0.01
         speedright_f = speedright_f + 0.01
         speedright_b = speedright_b - 0.1

         if speedleft_f < -1:
            speedleft_f = -1
         if speedleft_b >= 0.01:
            speedleft_b = 0.01
         if speedright_f >= 0.01:
            speedright_f = 0.01
         if speedright_b < -1:
            speedright_b = -1
            
         printscreen()            

      if(char == "R"):

         speedleft_f = speedleft_f + 0.01
         speedleft_b = speedleft_b - 0.1
         speedright_f = speedright_f - 0.1
         speedright_b = speedright_b + 0.01

         if speedleft_f >= 0.01:
            speedleft_f = 0.01
         if speedleft_b < -1:
            speedleft_b = -1
         if speedright_f < -1:
            speedright_f = -1
         if speedright_b >= 0.01:
            speedright_b = 0.01
            
         printscreen()            

      if(char == "s" or char == "S"):

         speedleft_f = speedleft_f - 0.1
         speedleft_b = speedleft_b - 0.1
         speedright_f = speedright_f - 0.1
         speedright_b = speedright_b - 0.1

         if speedleft_f < -1:
            speedleft_f = -1
         if speedleft_b < -1:
            speedleft_b = -1
         if speedright_f < -1:
            speedright_f = -1
         if speedright_b < -1:
            speedright_b = -1
            
         printscreen()            

      if(char == "q" or char == "Q"):

         speedleft_f = speedleft_f - 0.1
         speedleft_b = speedleft_b + 0.1
         speedright_f = speedright_f + 0.1
         speedright_b = speedright_b - 0.1

         if speedleft_f < -1:
            speedleft_f = -1
         if speedleft_b > 1:
            speedleft_b = 1
         if speedright_f > 1:
            speedright_f = 1
         if speedright_b < -1:
            speedright_b = -1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "e" or char == "E"):

         speedleft_f = speedleft_f + 0.1
         speedleft_b = speedleft_b - 0.1
         speedright_f = speedright_f - 0.1
         speedright_b = speedright_b + 0.1

         if speedleft_f > 1:
            speedleft_f = 1
         if speedleft_b < -1:
            speedleft_b = -1
         if speedright_f < -1:
            speedright_f = -1
         if speedright_b > 1:
            speedright_b = 1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "d" or char == "D"):

         speedleft_f = speedleft_f - 0.1
         speedleft_b = speedleft_b - 0.1
         speedright_f = speedright_f + 0.1
         speedright_b = speedright_b + 0.1

         if speedleft_f < -1:
            speedleft_f = -1
         if speedleft_b < -1:
            speedleft_b = -1
         if speedright_f > 1:
            speedright_f = 1
         if speedright_b > 1:
            speedright_b = 1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "a" or char == "A"):

         speedleft_f = speedleft_f + 0.1
         speedleft_b = speedleft_b + 0.1
         speedright_f = speedright_f - 0.1
         speedright_b = speedright_b - 0.1

         if speedleft_f > 1:
            speedleft_f = 1
         if speedleft_b > 1:
            speedleft_b = 1
         if speedright_f < -1:
            speedright_f = -1
         if speedright_b < -1:
            speedright_b = -1
         ##HBridge.setMotorLeft(speedleft)
         ##HBridge.setMotorRight(speedright)
         printscreen()

      if(char == "z" or char == "Z"):
         speedleft_f = 0
         speedleft_b = 0
         speedright_f = 0
         speedright_b = 0
         
         ##HBridge.setMotorRight(speedright)
         printscreen()         
         

      if(char == "x" or char == "X"):
         speedleft_f = 0
         speedleft_b = 0
         speedright_f = 0
         speedright_b = 0
         print ("Program Ended motorset 0")
         rospy.loginfo_once("ctrl+c exit")
         break

      speed.linear.x = speedleft_f
      speed.linear.y = speedleft_b
      speed.linear.z = speedright_f
      speed.angular.x = speedright_b
 
      char = ""
      
      pub.publish(speed)
