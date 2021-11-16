#!/usr/bin/env python
from __future__ import division
from Adafruit_PCA9685.PCA9685 import PCA9685
from geometry_msgs.msg import Twist
import rospy
import RPi.GPIO as io
io.setmode(io.BOARD)
import Adafruit_PCA9685
import time
io.setwarnings(False)
PCA9685_pwm = Adafruit_PCA9685.PCA9685()
PCA9685_pwm.set_pwm_freq(60)
duty_cycle = 4095
#setmotorleft
leftmotor_front_int1_pin = 21
leftmotor_front_int2_pin = 22
leftmotor_back_int1_pin = 11
leftmotor_back_int2_pin = 12
io.setup(leftmotor_front_int1_pin, io.OUT)
io.setup(leftmotor_front_int2_pin, io.OUT)
io.setup(leftmotor_back_int1_pin, io.OUT)
io.setup(leftmotor_back_int2_pin, io.OUT)
#setmotorright
rightmotor_front_int1_pin = 23
rightmotor_front_int2_pin = 19
rightmotor_back_int1_pin = 15
rightmotor_back_int2_pin = 16
io.setup(rightmotor_front_int1_pin, io.OUT)
io.setup(rightmotor_front_int2_pin, io.OUT)
io.setup(rightmotor_back_int1_pin, io.OUT)
io.setup(rightmotor_back_int2_pin, io.OUT)

io.setup(leftmotor_front_int1_pin, False)
io.setup(leftmotor_front_int2_pin, False)
io.setup(leftmotor_back_int1_pin, False)
io.setup(leftmotor_back_int2_pin, False)
io.setup(rightmotor_front_int1_pin, False)
io.setup(rightmotor_front_int2_pin, False)
io.setup(rightmotor_back_int1_pin, False)
io.setup(rightmotor_back_int2_pin, False)
PCA9685_pwm.set_pwm(0, 0, 0)
PCA9685_pwm.set_pwm(1, 0, 0)  
PCA9685_pwm.set_pwm(2, 0, 0)
PCA9685_pwm.set_pwm(3, 0, 0)
PCA9685_pwm.set_pwm(4, 0, 0)
PCA9685_pwm.set_pwm(5, 0, 0)  
PCA9685_pwm.set_pwm(6, 0, 0)
PCA9685_pwm.set_pwm(7, 0, 0)

def setMotorMode(motor, mode):
   if motor == "leftmotor_back":
      if mode == "reverse":
         io.output(leftmotor_back_int1_pin, True)
         io.output(leftmotor_back_int2_pin, False)
      elif  mode == "forward":
         io.output(leftmotor_back_int1_pin, False)
         io.output(leftmotor_back_int2_pin, True)
      else:
         io.output(leftmotor_back_int1_pin, False)
         io.output(leftmotor_back_int2_pin, False)
   elif motor == "leftmotor_front":
      if mode == "reverse":
         io.output(leftmotor_front_int1_pin, False)
         io.output(leftmotor_front_int2_pin, True)      
      elif  mode == "forward":
         io.output(leftmotor_front_int1_pin, True)
         io.output(leftmotor_front_int2_pin, False)
      else:
         io.output(leftmotor_front_int1_pin, False)
         io.output(leftmotor_front_int2_pin, False)        
   elif motor == "rightmotor_back":
      if mode == "reverse":
         io.output(rightmotor_back_int1_pin, True)
         io.output(rightmotor_back_int2_pin, False)
      elif  mode == "forward":
         io.output(rightmotor_back_int1_pin, False)
         io.output(rightmotor_back_int2_pin, True)
      else:
         io.output(rightmotor_back_int1_pin, False)
         io.output(rightmotor_back_int2_pin, False)
   elif motor == "rightmotor_front":
      if mode == "reverse":
         io.output(rightmotor_front_int1_pin, False)
         io.output(rightmotor_front_int2_pin, True)      
      elif  mode == "forward":
         io.output(rightmotor_front_int1_pin, True)
         io.output(rightmotor_front_int2_pin, False)
      else:
         io.output(rightmotor_front_int1_pin, False)
         io.output(rightmotor_front_int2_pin, False)
   else:
      io.output(leftmotor_back_int1_pin, False)
      io.output(leftmotor_back_int2_pin, False)
      io.output(leftmotor_front_int1_pin, False)
      io.output(leftmotor_front_int2_pin, False)
	  
      io.output(rightmotor_back_int1_pin, False)
      io.output(rightmotor_back_int2_pin, False)
      io.output(rightmotor_front_int1_pin, False)
      io.output(rightmotor_front_int2_pin, False)

def setMotorLeftBack(power):
   int(power)
   if power < 0:
      setMotorMode("leftmotor_back", "reverse")
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(0, 0, pwm)
      PCA9685_pwm.set_pwm(1, 0, 0)   
   elif power > 0:
      setMotorMode("leftmotor_back", "forward")
      pwm = int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(0, 0, 0)
      PCA9685_pwm.set_pwm(1, 0, pwm)  	  
   else:
      PCA9685_pwm.set_pwm(0, 0, 0)
      PCA9685_pwm.set_pwm(1, 0, 0)  
      PCA9685_pwm.set_pwm(2, 0, 0)
      PCA9685_pwm.set_pwm(3, 0, 0)
      PCA9685_pwm.set_pwm(4, 0, 0)
      PCA9685_pwm.set_pwm(5, 0, 0)  
      PCA9685_pwm.set_pwm(6, 0, 0)
      PCA9685_pwm.set_pwm(7, 0, 0)		

def setMotorLeftFront(power):
   int(power)
   if power < 0:
      setMotorMode("leftmotor_front", "reverse")
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(4, 0, pwm)
      PCA9685_pwm.set_pwm(5, 0, 0)  	  
   elif power > 0:
      setMotorMode("leftmotor_front", "forward")
      pwm = int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(4, 0, 0)
      PCA9685_pwm.set_pwm(5, 0, pwm)  	  
   else:
      PCA9685_pwm.set_pwm(0, 0, 0)
      PCA9685_pwm.set_pwm(1, 0, 0)  
      PCA9685_pwm.set_pwm(2, 0, 0)
      PCA9685_pwm.set_pwm(3, 0, 0)
      PCA9685_pwm.set_pwm(4, 0, 0)
      PCA9685_pwm.set_pwm(5, 0, 0)  
      PCA9685_pwm.set_pwm(6, 0, 0)
      PCA9685_pwm.set_pwm(7, 0, 0)		

def setMotorRightBack(power):
   int(power)
   if power < 0:
      setMotorMode("rightmotor_back", "reverse")
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(2, 0, pwm)
      PCA9685_pwm.set_pwm(3, 0, 0)  	  
   elif power > 0:
      setMotorMode("rightmotor_back", "forward")
      pwm = int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(2, 0, 0)
      PCA9685_pwm.set_pwm(3, 0, pwm)  	  
   else:
      PCA9685_pwm.set_pwm(0, 0, 0)
      PCA9685_pwm.set_pwm(1, 0, 0)  
      PCA9685_pwm.set_pwm(2, 0, 0)
      PCA9685_pwm.set_pwm(3, 0, 0)
      PCA9685_pwm.set_pwm(4, 0, 0)
      PCA9685_pwm.set_pwm(5, 0, 0)  
      PCA9685_pwm.set_pwm(6, 0, 0)
      PCA9685_pwm.set_pwm(7, 0, 0)
      
def setMotorRightFront(power):
   int(power)
   if power < 0:
      setMotorMode("rightmotor_front", "reverse")
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(6, 0, pwm)
      PCA9685_pwm.set_pwm(7, 0, 0)  	  
   elif power > 0:
      setMotorMode("rightmotor_front", "reverse")
      pwm = int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(6, 0, 0)
      PCA9685_pwm.set_pwm(7, 0, pwm)  	  
   else:
      PCA9685_pwm.set_pwm(0, 0, 0)
      PCA9685_pwm.set_pwm(1, 0, 0)  
      PCA9685_pwm.set_pwm(2, 0, 0)
      PCA9685_pwm.set_pwm(3, 0, 0)
      PCA9685_pwm.set_pwm(4, 0, 0)
      PCA9685_pwm.set_pwm(5, 0, 0)  
      PCA9685_pwm.set_pwm(6, 0, 0)
      PCA9685_pwm.set_pwm(7, 0, 0)
           
def exit():
   io.output(leftmotor_back_int1_pin, False)
   io.output(leftmotor_back_int2_pin, False)
   io.output(leftmotor_front_int1_pin, False)
   io.output(leftmotor_front_int2_pin, False)
   
   io.output(rightmotor_back_int1_pin, False)
   io.output(rightmotor_back_int2_pin, False)
   io.output(rightmotor_front_int1_pin, False)
   io.output(rightmotor_front_int2_pin, False) 
   io.cleanup()
   PCA9685_pwm.set_pwm(0, 0, 0)
   PCA9685_pwm.set_pwm(1, 0, 0)  
   PCA9685_pwm.set_pwm(2, 0, 0)
   PCA9685_pwm.set_pwm(3, 0, 0)
   PCA9685_pwm.set_pwm(4, 0, 0)
   PCA9685_pwm.set_pwm(5, 0, 0)  
   PCA9685_pwm.set_pwm(6, 0, 0)
   PCA9685_pwm.set_pwm(7, 0, 0)


def setMotor(msg):
   setMotorLeftFront(msg.linear.x)
   setMotorLeftBack(msg.linear.y)
   setMotorRightFront(msg.linear.z)
   setMotorRightBack(msg.angular.x)
   rospy.loginfo(msg.linear.x)
   rospy.loginfo(msg.linear.y)


if __name__ == '__main__':
   print ("Starting motor node")
   rospy.init_node('motors')
   #rospy.Subscriber('cmd_vel', String, queue_size=10)
   rospy.Subscriber('cmd_vel', Twist, setMotor)
   rospy.spin()