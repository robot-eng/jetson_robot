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
leftmotor_int1_pin = 21
leftmotor_int2_pin = 22
leftmotor_int3_pin = 11
leftmotor_int4_pin = 12
io.setup(leftmotor_int1_pin, io.OUT)
io.setup(leftmotor_int2_pin, io.OUT)
io.setup(leftmotor_int3_pin, io.OUT)
io.setup(leftmotor_int4_pin, io.OUT)
#setmotorright
rightmotor_int1_pin = 23
rightmotor_int2_pin = 19
rightmotor_int3_pin = 15
rightmotor_int4_pin = 16
io.setup(rightmotor_int1_pin, io.OUT)
io.setup(rightmotor_int2_pin, io.OUT)
io.setup(rightmotor_int3_pin, io.OUT)
io.setup(rightmotor_int4_pin, io.OUT)

io.output(leftmotor_int1_pin, True)
io.output(leftmotor_int2_pin, True)
io.output(leftmotor_int3_pin, True)
io.output(leftmotor_int4_pin, True)
io.output(rightmotor_int1_pin, True)
io.output(rightmotor_int2_pin, True)
io.output(rightmotor_int3_pin, True)
io.output(rightmotor_int4_pin, True)

def setMotorMode(motor, mode):
   if motor == "leftmotor_f":
      if mode == "reverse":
         io.output(leftmotor_int1_pin, True)
         io.output(leftmotor_int2_pin, False)
      elif  mode == "forward":
         io.output(leftmotor_int1_pin, False)
         io.output(leftmotor_int2_pin, True)
      else:
         io.output(leftmotor_int1_pin, False)
         io.output(leftmotor_int2_pin, False)
   if motor == "leftmotor_b":
      if mode == "reverse":
         io.output(leftmotor_int3_pin, True)
         io.output(leftmotor_int4_pin, False)
      elif  mode == "forward":
         io.output(leftmotor_int3_pin, False)
         io.output(leftmotor_int4_pin, True)
      else:
         io.output(leftmotor_int3_pin, False)
         io.output(leftmotor_int4_pin, False)
   elif motor == "rightmotor_f":
      if mode == "reverse":
         io.output(rightmotor_int1_pin, False)
         io.output(rightmotor_int2_pin, True)    
      elif  mode == "forward":
         io.output(rightmotor_int1_pin, True)
         io.output(rightmotor_int2_pin, False)
      else:
         io.output(rightmotor_int1_pin, False)
         io.output(rightmotor_int2_pin, False)
   elif motor == "rightmotor_b":
      if mode == "reverse":
         io.output(rightmotor_int3_pin, False)
         io.output(rightmotor_int4_pin, True)    
      elif  mode == "forward":
         io.output(rightmotor_int3_pin, True)
         io.output(rightmotor_int4_pin, False)
      else:
         io.output(rightmotor_int3_pin, False)
         io.output(rightmotor_int4_pin, False)
   else:
      io.output(leftmotor_int1_pin, False)
      io.output(leftmotor_int2_pin, False)
      io.output(leftmotor_int3_pin, False)
      io.output(leftmotor_int4_pin, False)
      io.output(rightmotor_int1_pin, False)
      io.output(rightmotor_int2_pin, False)
      io.output(rightmotor_int3_pin, False)
      io.output(rightmotor_int4_pin, False)

def setMotorLeft_f(power):
   int(power)
   if power < 0:
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(0, 0, pwm)
      PCA9685_pwm.set_pwm(1, 0, 0)   
   elif power > 0:
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

def setMotorLeft_b(power):
   int(power)
   if power < 0:
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(4, 0, pwm)
      PCA9685_pwm.set_pwm(5, 0, 0)    
   elif power > 0:
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

def setMotorRight_f(power):
   int(power)
   if power < 0:
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(2, 0, pwm)
      PCA9685_pwm.set_pwm(3, 0, 0)   	  
   elif power > 0:
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

def setMotorRight_b(power):
   int(power)
   if power < 0:
      pwm = -int(duty_cycle * power)
      if pwm > duty_cycle:
         pwm = duty_cycle
      PCA9685_pwm.set_pwm(6, 0, pwm)
      PCA9685_pwm.set_pwm(7, 0, 0)   	  
   elif power > 0:
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
   io.output(leftmotor_int1_pin, False)
   io.output(leftmotor_int2_pin, False)
   io.output(leftmotor_int3_pin, False)
   io.output(leftmotor_int4_pin, False)
   io.output(rightmotor_int1_pin, False)
   io.output(rightmotor_int2_pin, False)
   io.output(rightmotor_int3_pin, False)
   io.output(rightmotor_int4_pin, False)
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
   setMotorLeft_f(msg.linear.x)
   setMotorLeft_b(msg.linear.y)
   setMotorRight_f(msg.linear.z)
   setMotorRight_b(msg.angular.x)
   rospy.loginfo(msg.linear.x)
   rospy.loginfo(msg.linear.y)


if __name__ == '__main__':
   print ("Starting motor node")
   rospy.init_node('motors')
   #rospy.Subscriber('cmd_vel', String, queue_size=10)
   rospy.Subscriber('cmd_vel', Twist, setMotor)
   rospy.spin()
