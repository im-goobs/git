from appJar import *
import RPi.GPIO as GPIO
import time

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #Sirens


def ButtonHandler(select):
	if select == "Sirens ON":
                GPIO.output(11, GPIO.HIGH)
                program.infoBox("Message","Sirens ON")
        elif select == "Sirens OFF":
                GPIO.output(11, GPIO.LOW)
                program.infoBox("Message","Sirens OFF")



#Style
program = gui("Title", "500x300")
program.setBg("steel blue")

#Buttons
program.addButtons(["Sirens ON", "Sirens OFF"], ButtonHandler)


#POS
program.setSize("Fullscreen")




program.go()
GPIO.cleanup()


