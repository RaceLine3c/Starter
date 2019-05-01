#author: RaceLine

import time #import this package to use sleep function
import RPi.GPIO as GPIO #import this package to interact with GPIO pins
import os #import this package to play sound files
from nanpy import ArduinoApi #import this package to use arduino on raspberry pi
from nanpy import SerialManager #connnect arduino on raspberry pi with serial port

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.OUT) #set the GPIO pin for the first LED light as output
GPIO.setup(21, GPIO.OUT) #set the GPIO pin for the second LED light as output
GPIO.setup(23, GPIO.OUT) #set the GPIO pin for the third LED light as output

GPIO.setup(4, GPIO.IN) #set the GPIO pin for PIR sensor as input

#initialise Arduino with serial port
connection = SerialManager()
a = ArduinoApi(connection = connection)

#initialise digital port to L298n motor driver
a.pinMode(2, a.OUTPUT) # ENA
a.pinMode(3, a.OUTPUT) # IN1
a.pinMode(4, a.OUTPUT) # IN2
a.pinMode(5, a.OUTPUT) # ENB
a.pinMode(6, a.OUTPUT) # IN3
a.pinMode(7, a.OUTPUT) # IN4

a.digitalWrite(2, a.HIGH) # ENA
a.digitalWrite(5, a.HIGH) # ENB

counter = 0

try:
    while True:
        input = GPIO.input(4) #set the current value received by PIR sensor
        
        if input == 0:
            print("Sensing Motion : " + str(counter))
            
            GPIO.output(19, GPIO.LOW) #turn off the first LED light
            GPIO.output(21, GPIO.LOW) #turn off the second LED light
            GPIO.output(23, GPIO.LOW) #turn off the third LED light
            
            counter = counter + 1
            time.sleep(1)
            
        elif input == 1:
            print("Motion Detected")

            os.system("omxplayer -o local hey.ogg") #play the sound on speaker for people come
            
            os.system("omxplayer -o local 3.ogg") #play the sound of counter at 1 on speaker
            GPIO.output(19, GPIO.HIGH) #turn on the first LED light
            
            os.system("omxplayer -o local 2.ogg") #play the sound of counter at 2 on speaker
            GPIO.output(21, GPIO.HIGH) #turn on the second LED light
            
            os.system("omxplayer -o local 1.ogg") #play the sound of counter at 3 on speaker
            GPIO.output(23, GPIO.HIGH) #turn on the third LED light
            
            os.system("omxplayer -o local start.ogg") #play the sound of the f1 on speaker
            
            time.sleep(0.1)
            
            GPIO.output(19, GPIO.LOW) #turn off the first LED light
            GPIO.output(21, GPIO.LOW) #turn off the second LED light
            GPIO.output(23, GPIO.LOW) #turn off the third LED light

            time.sleep(0.2)

            GPIO.output(19, GPIO.HIGH) #turn on the first LED light
            GPIO.output(21, GPIO.HIGH) #turn on the second LED light
            GPIO.output(23, GPIO.HIGH) #turn on the third LED light
            
            time.sleep(0.2)
            
            GPIO.output(19, GPIO.LOW) #turn off the first LED light
            GPIO.output(21, GPIO.LOW) #turn off the second LED light
            GPIO.output(23, GPIO.LOW) #turn off the third LED light

            time.sleep(0.2)

            GPIO.output(19, GPIO.HIGH) #turn on the first LED light
            GPIO.output(21, GPIO.HIGH) #turn on the second LED light
            GPIO.output(23, GPIO.HIGH) #turn on the third LED light
            
            time.sleep(0.2)
            
            GPIO.output(19, GPIO.LOW) #turn off the first LED light
            GPIO.output(21, GPIO.LOW) #turn off the second LED light
            GPIO.output(23, GPIO.LOW) #turn off the third LED light
			
	    #program the motor
            a.digitalWrite(3, a.LOW)
            a.digitalWrite(4, a.HIGH)
            a.digitalWrite(6, a.HIGH)
            a.digitalWrite(7, a.LOW)

            time.sleep(1)

            a.digitalWrite(3, a.LOW)
            a.digitalWrite(4, a.HIGH)
            a.digitalWrite(6, a.LOW)
            a.digitalWrite(7, a.HIGH)

            time.sleep(1)

            a.digitalWrite(3, a.HIGH)
            a.digitalWrite(4, a.LOW)
            a.digitalWrite(6, a.LOW)
            a.digitalWrite(7, a.HIGH)

            time.sleep(1)

            a.digitalWrite(3, a.HIGH)
            a.digitalWrite(4, a.LOW)
            a.digitalWrite(6, a.HIGH)
            a.digitalWrite(7, a.LOW)

            time.sleep(1)
            
finally: #If the program is interrupted, this block will be executed
    GPIO.output(19, GPIO.LOW) #make sure to turn the first LED light off
    GPIO.output(21, GPIO.LOW) #make sure to turn the second LED light off
    GPIO.output(23, GPIO.LOW) #make sure to turn the third LED light off

    a.digitalWrite(2, a.LOW) # ENA
    a.digitalWrite(3, a.LOW) # IN1
    a.digitalWrite(4, a.LOW) # IN2
    a.digitalWrite(5, a.LOW) # ENB
    a.digitalWrite(6, a.LOW) # IN3
    a.digitalWrite(7, a.LOW) # IN4
    
    GPIO.cleanup() #make sure we are shutting down our program cleanly
