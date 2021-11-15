#!/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20161120
# Version:   2.0
# Homepage:   http://custom-build-robots.com

# Dieses Programm wurde fuer die Ansteuerung der linken und rechten
# Motoren des Roboter-Autos entwickelt. Es geht dabei davon aus,
# dass eine L298N H-Bruecke als Motortreiber eingesetzt wird.

# Dieses Programm muss von einem uebergeordneten Programm aufgerufen 
# werden, dass die Steuerung des Programmes L298NHBridge übernimmt.

# Es wird die Klasse RPi.GPIO importiert, die die Ansteuerung
# der GPIO Pins des Raspberry Pi ermoeglicht.
import RPi.GPIO as io
io.setmode(io.BCM)

# Die Variable PWM_MAX gibt die maximale Drehgeschwindigkeit der 
# Motoren als Prozentwert vor.
# Die Geschwindigkeit wird initial auf 70% der max Leistung der
# H-Bruecke gedrosselt um am Anfang mit der Steuerung des Roboter
# Autos besser zurecht zu kommen. Soll das Roboter-Auto schneller 
# fahren kann hier der Wert von 70% auf maximal 100% gesetzt werden.

PWM_MAX = 70

# Mit dem folgenden Aufruf werden eventuelle Warnungen die die 
# Klasse RPi.GPIO ausgibt deaktiviert.
io.setwarnings(False)

# Im folgenden Programmabschnitt wird die logische Verkabelung des 
# Raspberry Pi im Programm abgebildet. Dazu werden den vom Motor 
# Treiber bekannten Pins die GPIO Adressen zugewiesen.

# --- START KONFIGURATION GPIO Adressen ---
# Links
# Linker Motor hinen
L_ENA = 20
L_IN1 = 6
L_IN2 = 13
# Linker Motor vorn
L_ENB = 21
L_IN3 = 19
L_IN4 = 26

#Rechts
# Rechter Motor hinten
R_ENA = 18
R_IN1 = 4
R_IN2 = 17
# Recher Motor vorn
R_ENB = 23
R_IN3 = 27
R_IN4 = 22
# --- ENDE KONFIGURATION GPIO Adressen ---

#
# Linke Motoren
#
# Der Variable leftmotor_back_in1_pin wird die Varibale IN1 zugeorndet. 
# Der Variable leftmotor_back_in2_pin wird die Varibale IN2 zugeorndet. 
leftmotor_back_in1_pin = L_IN1
leftmotor_back_in2_pin = L_IN2
# Beide Variablen leftmotor_back_in1_pin und leftmotor_back_in2_pin werden als
# Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehrichtung der Motoren gesteuert.
io.setup(leftmotor_back_in1_pin, io.OUT)
io.setup(leftmotor_back_in2_pin, io.OUT)

# Der Variable leftmotor_front_in1_pin wird die Varibale IN1 zugeorndet. 
# Der Variable leftmotor_front_in2_pin wird die Varibale IN2 zugeorndet. 
leftmotor_front_in1_pin = L_IN3
leftmotor_front_in2_pin = L_IN4
# Beide Variablen leftmotor_front_in1_pin und leftmotor_front_in2_pin werden 
# als Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehrichtung der Motoren gesteuert.
io.setup(leftmotor_front_in1_pin, io.OUT)
io.setup(leftmotor_front_in2_pin, io.OUT)

# Die GPIO Pins des Raspberry Pi werden initial auf False gesetzt.
# So ist sichger gestellt, dass kein HIGH Signal anliegt und der 
# Motor Treiber nicht unbeabsichtigt aktiviert wird.
io.output(leftmotor_back_in1_pin, False)
io.output(leftmotor_back_in2_pin, False)
io.output(leftmotor_front_in1_pin, False)
io.output(leftmotor_front_in2_pin, False)

# Der Variable leftmotorpwm_back_pin wird die Varibale ENA zugeorndet.
# Der Variable rightmotorpwm_front_pin wird die Varibale ENB zugeorndet.
leftmotorpwm_back_pin = L_ENA
rightmotorpwm_front_pin = L_ENB

# Die Beide Variablen leftmotorpwm_back_pin und rightmotorpwm_front_pin werden 
# als Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehgeschwindigkeit der Motoren über ein PWM Signal gesteuert.
io.setup(leftmotorpwm_back_pin, io.OUT)
io.setup(rightmotorpwm_front_pin, io.OUT)

# Die Beide Variablen leftmotorpwm_back_pin und rightmotorpwm_front_pin werden 
# zusätzlich zu Ihrer Eigenschaft als Ausgaenge als "PWM" Ausgaenge
# definiert.
leftmotorpwm_back = io.PWM(leftmotorpwm_back_pin,100)
leftmotorpwm_front = io.PWM(rightmotorpwm_front_pin,100)

# Die linke Motoren steht still, da das PWM Signale mit 
# ChangeDutyCycle(0) auf 0 gesetzt wurde.
leftmotorpwm_back.start(0)
leftmotorpwm_back.ChangeDutyCycle(0)

# Die rechten Motoren steht still, da das PWM Signale mit 
# ChangeDutyCycle(0) auf 0 gesetzt wurde.
leftmotorpwm_front.start(0)
leftmotorpwm_front.ChangeDutyCycle(0)

#
# Rechte Motoren
#
# Der Variable rightmotor_back_in1_pin wird die Varibale IN1 zugeorndet. 
# Der Variable rightmotor_back_in2_pin wird die Varibale IN2 zugeorndet. 
rightmotor_back_in1_pin = R_IN1
rightmotor_back_in2_pin = R_IN2
# Beide Variablen rightmotor_back_in1_pin und rightmotor_back_in2_pin werden als
# Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehrichtung der Motoren gesteuert.
io.setup(rightmotor_back_in1_pin, io.OUT)
io.setup(rightmotor_back_in2_pin, io.OUT)

# Der Variable rightmotor_front_in1_pin wird die Varibale IN1 zugeorndet. 
# Der Variable rightmotor_front_in2_pin wird die Varibale IN2 zugeorndet. 
rightmotor_front_in1_pin = R_IN3
rightmotor_front_in2_pin = R_IN4
# Beide Variablen rightmotor_front_in1_pin und rightmotor_front_in2_pin werden 
# als Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehrichtung der Motoren gesteuert.
io.setup(rightmotor_front_in1_pin, io.OUT)
io.setup(rightmotor_front_in2_pin, io.OUT)

# Die GPIO Pins des Raspberry Pi werden initial auf False gesetzt.
# So ist sichger gestellt, dass kein HIGH Signal anliegt und der 
# Motor Treiber nicht unbeabsichtigt aktiviert wird.
io.output(rightmotor_back_in1_pin, False)
io.output(rightmotor_back_in2_pin, False)
io.output(rightmotor_front_in1_pin, False)
io.output(rightmotor_front_in2_pin, False)

# Der Variable rightmotorpwm_back_pin wird die Varibale ENA zugeorndet.
# Der Variable rightmotorpwm_front_pin wird die Varibale ENB zugeorndet.
rightmotorpwm_back_pin = R_ENA
rightmotorpwm_front_pin = R_ENB

# Die Beide Variablen rightmotorpwm_back_pin und rightmotorpwm_front_pin werden 
# als Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehgeschwindigkeit der Motoren über ein PWM Signal gesteuert.
io.setup(rightmotorpwm_back_pin, io.OUT)
io.setup(rightmotorpwm_front_pin, io.OUT)

# Die Beide Variablen rightmotorpwm_back_pin und rightmotorpwm_front_pin werden 
# zusätzlich zu Ihrer Eigenschaft als Ausgaenge als "PWM" Ausgaenge
# definiert.
rightmotorpwm_back = io.PWM(rightmotorpwm_back_pin,100)
rightmotorpwm_front = io.PWM(rightmotorpwm_front_pin,100)

# Die linke Motoren steht still, da das PWM Signale mit 
# ChangeDutyCycle(0) auf 0 gesetzt wurde.
rightmotorpwm_back.start(0)
rightmotorpwm_back.ChangeDutyCycle(0)

# Die rechten Motoren steht still, da das PWM Signale mit 
# ChangeDutyCycle(0) auf 0 gesetzt wurde.
rightmotorpwm_front.start(0)
rightmotorpwm_front.ChangeDutyCycle(0)

#
#
# Steuerung Roboter
#
#
# Die Funktion setMotorMode(motor, mode) legt die Drehrichtung der 
# Motoren fest. Die Funktion verfügt über zwei Eingabevariablen.
# motor      -> diese Variable legt fest ob der linke oder rechte 
#              Motor ausgewaehlt wird.
# mode      -> diese Variable legt fest welcher Modus gewaehlt ist
# Beispiel:
# setMotorMode(leftmotor, forward)   Der linke Motor ist gewaehlt
#                                   und dreht vorwaerts .
# setMotorMode(rightmotor, reverse)   Der rechte Motor ist ausgewaehlt 
#                                   und dreht rueckwaerts.
# setMotorMode(rightmotor, stopp)   Der rechte Motor ist ausgewaehlt
#                                   der gestoppt wird.

def setMotorMode(motor, mode):
   if motor == "leftmotor_back":
      if mode == "reverse":
         io.output(leftmotor_back_in1_pin, True)
         io.output(leftmotor_back_in2_pin, False)
      elif  mode == "forward":
         io.output(leftmotor_back_in1_pin, False)
         io.output(leftmotor_back_in2_pin, True)
      else:
         io.output(leftmotor_back_in1_pin, False)
         io.output(leftmotor_back_in2_pin, False)
   elif motor == "leftmotor_front":
      if mode == "reverse":
         io.output(leftmotor_front_in1_pin, False)
         io.output(leftmotor_front_in2_pin, True)      
      elif  mode == "forward":
         io.output(leftmotor_front_in1_pin, True)
         io.output(leftmotor_front_in2_pin, False)
      else:
         io.output(leftmotor_front_in1_pin, False)
         io.output(leftmotor_front_in2_pin, False)
   elif motor == "rightmotor_back":
      if mode == "reverse":
         io.output(rightmotor_back_in1_pin, True)
         io.output(rightmotor_back_in2_pin, False)
      elif  mode == "forward":
         io.output(rightmotor_back_in1_pin, False)
         io.output(rightmotor_back_in2_pin, True)
      else:
         io.output(rightmotor_back_in1_pin, False)
         io.output(rightmotor_back_in2_pin, False)
   elif motor == "rightmotor_front":
      if mode == "reverse":
         io.output(rightmotor_front_in1_pin, False)
         io.output(rightmotor_front_in2_pin, True)      
      elif  mode == "forward":
         io.output(rightmotor_front_in1_pin, True)
         io.output(rightmotor_front_in2_pin, False)
      else:
         io.output(rightmotor_front_in1_pin, False)
         io.output(rightmotor_front_in2_pin, False)
   else:
      io.output(leftmotor_back_in1_pin, False)
      io.output(leftmotor_back_in2_pin, False)
      io.output(leftmotor_front_in1_pin, False)
      io.output(leftmotor_front_in2_pin, False)
	  
      io.output(rightmotor_back_in1_pin, False)
      io.output(rightmotor_back_in2_pin, False)
      io.output(rightmotor_front_in1_pin, False)
      io.output(rightmotor_front_in2_pin, False)
#
#
# Linke Motoren
#
# 	  
# Die Funktion setMotorLeft(power) setzt die Geschwindigkeit der 
# linken Motoren. Die Geschwindigkeit wird als Wert zwischen -1
# und 1 uebergeben. Bei einem negativen Wert sollen sich die Motoren 
# rueckwaerts drehen ansonsten vorwaerts. 
# Anschliessend werden aus den uebergebenen Werten die notwendigen 
# %-Werte fuer das PWM Signal berechnet.

# Beispiel Left Motor Back:
# Die Geschwindigkeit kann mit +1 (max) und -1 (min) gesetzt werden.
# Das Beispielt erklaert wie die Geschwindigkeit berechnet wird.
# SetMotorLeft(0)     -> der linke Motor dreht mit 0% ist gestoppt
# SetMotorLeft(0.75)  -> der linke Motor dreht mit 75% vorwaerts
# SetMotorLeft(-0.5)  -> der linke Motor dreht mit 50% rueckwaerts
# SetMotorLeft(1)     -> der linke Motor dreht mit 100% vorwaerts
def setMotorLeftBack(power):
   int(power)
   if power < 0:
      # Rueckwaertsmodus fuer den linken Motor
      setMotorMode("leftmotor_back", "reverse")
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   elif power > 0:
      # Vorwaertsmodus fuer den linken Motor
      setMotorMode("leftmotor_back", "forward")
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   else:
      # Stoppmodus fuer den linken Motor
      setMotorMode("leftmotor_back", "stopp")
      pwm = 0
   leftmotorpwm_back.ChangeDutyCycle(pwm)

# Die Funktion setMotorRight(power) setzt die Geschwindigkeit der 
# rechten Motoren. Die Geschwindigkeit wird als Wert zwischen -1 
# und 1 uebergeben. Bei einem negativen Wert sollen sich die Motoren 
# rueckwaerts drehen ansonsten vorwaerts. 
# Anschliessend werden aus den uebergebenen Werten die notwendigen 
# %-Werte fuer das PWM Signal berechnet.

# Beispiel Left Motor Front:
# Die Geschwindigkeit kann mit +1 (max) und -1 (min) gesetzt werden.
# Das Beispielt erklaert wie die Geschwindigkeit berechnet wird.
# setMotorRight(0)     -> der linke Motor dreht mit 0% ist gestoppt
# setMotorRight(0.75)  -> der linke Motor dreht mit 75% vorwaerts
# setMotorRight(-0.5)  -> der linke Motor dreht mit 50% rueckwaerts
# setMotorRight(1)     -> der linke Motor dreht mit 100% vorwaerts   
   
def setMotorLeftFront(power):
   int(power)
   if power < 0:
      # Rueckwaertsmodus fuer den rechten Motor
      setMotorMode("leftmotor_front", "reverse")
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   elif power > 0:
      # Vorwaertsmodus fuer den rechten Motor
      setMotorMode("leftmotor_front", "forward")
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   else:
      # Stoppmodus fuer den rechten Motor
      setMotorMode("leftmotor_front", "stopp")
      pwm = 0
   leftmotorpwm_front.ChangeDutyCycle(pwm)

#
#
# Rechte Motoren
#
#   
# Die Funktion setMotorLeft(power) setzt die Geschwindigkeit der 
# linken Motoren. Die Geschwindigkeit wird als Wert zwischen -1
# und 1 uebergeben. Bei einem negativen Wert sollen sich die Motoren 
# rueckwaerts drehen ansonsten vorwaerts. 
# Anschliessend werden aus den uebergebenen Werten die notwendigen 
# %-Werte fuer das PWM Signal berechnet.

# Beispiel Left Motor Back:
# Die Geschwindigkeit kann mit +1 (max) und -1 (min) gesetzt werden.
# Das Beispielt erklaert wie die Geschwindigkeit berechnet wird.
# SetMotorLeft(0)     -> der linke Motor dreht mit 0% ist gestoppt
# SetMotorLeft(0.75)  -> der linke Motor dreht mit 75% vorwaerts
# SetMotorLeft(-0.5)  -> der linke Motor dreht mit 50% rueckwaerts
# SetMotorLeft(1)     -> der linke Motor dreht mit 100% vorwaerts
def setMotorRightBack(power):
   int(power)
   if power < 0:
      # Rueckwaertsmodus fuer den linken Motor
      setMotorMode("rightmotor_back", "reverse")
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   elif power > 0:
      # Vorwaertsmodus fuer den linken Motor
      setMotorMode("rightmotor_back", "forward")
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   else:
      # Stoppmodus fuer den linken Motor
      setMotorMode("rightmotor_back", "stopp")
      pwm = 0
   rightmotorpwm_back.ChangeDutyCycle(pwm)

# Die Funktion setMotorRight(power) setzt die Geschwindigkeit der 
# rechten Motoren. Die Geschwindigkeit wird als Wert zwischen -1 
# und 1 uebergeben. Bei einem negativen Wert sollen sich die Motoren 
# rueckwaerts drehen ansonsten vorwaerts. 
# Anschliessend werden aus den uebergebenen Werten die notwendigen 
# %-Werte fuer das PWM Signal berechnet.

# Beispiel Left Motor Front:
# Die Geschwindigkeit kann mit +1 (max) und -1 (min) gesetzt werden.
# Das Beispielt erklaert wie die Geschwindigkeit berechnet wird.
# setMotorRight(0)     -> der linke Motor dreht mit 0% ist gestoppt
# setMotorRight(0.75)  -> der linke Motor dreht mit 75% vorwaerts
# setMotorRight(-0.5)  -> der linke Motor dreht mit 50% rueckwaerts
# setMotorRight(1)     -> der linke Motor dreht mit 100% vorwaerts   
   
def setMotorRightFront(power):
   int(power)
   if power < 0:
      # Rueckwaertsmodus fuer den rechten Motor
      setMotorMode("rightmotor_front", "reverse")
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   elif power > 0:
      # Vorwaertsmodus fuer den rechten Motor
      setMotorMode("rightmotor_front", "forward")
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
   else:
      # Stoppmodus fuer den rechten Motor
      setMotorMode("rightmotor_front", "stopp")
      pwm = 0
   rightmotorpwm_front.ChangeDutyCycle(pwm)   
   
   
# Die Funktion exit() setzt die Ausgaenge die den Motor Treiber 
# steuern auf False. So befindet sich der Motor Treiber nach dem 
# Aufruf derFunktion in einem gesicherten Zustand und die Motoren 
# sind gestopped.
def exit():
   io.output(leftmotor_back_in1_pin, False)
   io.output(leftmotor_back_in2_pin, False)
   io.output(leftmotor_front_in1_pin, False)
   io.output(leftmotor_front_in2_pin, False)
   
   io.output(rightmotor_back_in1_pin, False)
   io.output(rightmotor_back_in2_pin, False)
   io.output(rightmotor_front_in1_pin, False)
   io.output(rightmotor_front_in2_pin, False) 
   io.cleanup()
   
# Ende des Programmes