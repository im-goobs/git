from appJar import *
import RPi.GPIO as GPIO
import time

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT) #Bay 1
GPIO.setup(5, GPIO.OUT) #Bay 2
GPIO.setup(7, GPIO.OUT) #Bay 3
GPIO.setup(11, GPIO.OUT) #Bay 4
GPIO.setup(13, GPIO.OUT) #Auto
GPIO.setup(15, GPIO.OUT) # Changer

def ButtonHandler(select):
	if select == "Bay One ON":
		GPIO.output(3, GPIO.HIGH)
		program.infoBox("Message","Bay One Siren ON")
	elif select == "Bay One OFF":
                GPIO.output(3, GPIO.LOW)
		program.infoBox("Message","Bay One Siren OFF")
	elif select == "Bay Two ON":
                GPIO.output(5, GPIO.HIGH)
                program.infoBox("Message","Bay Two Siren ON")
	elif select == "Bay Two OFF":
                GPIO.output(5, GPIO.LOW)
                program.infoBox("Message","Bay Two Siren OFF")
	elif select == "Bay Three ON":
                GPIO.output(7, GPIO.HIGH)
                program.infoBox("Message","Bay Three Siren ON")
	elif select == "Bay Three OFF":
                GPIO.output(7, GPIO.LOW)
                program.infoBox("Message","Bay Three Siren OFF")
	elif select == "Bay Four ON":
                GPIO.output(11, GPIO.HIGH)
                program.infoBox("Message","Bay Four Siren ON")
        elif select == "Bay Four OFF":
                GPIO.output(11, GPIO.LOW)
                program.infoBox("Message","Bay Four Siren OFF")
	elif select == "Bay Auto ON":
                GPIO.output(13, GPIO.HIGH)
                program.infoBox("Message","Bay Auto Siren ON")
        elif select == "Bay Auto OFF":
                GPIO.output(13, GPIO.LOW)
                program.infoBox("Message","Bay Auto Siren OFF")
	elif select == "Changer ON":
                GPIO.output(15, GPIO.HIGH)
                program.infoBox("Message","Changer Siren ON")
        elif select == "Changer OFF":
                GPIO.output(15, GPIO.LOW)
                program.infoBox("Message","Changer Siren OFF")



#Style
program = gui("Title", "500x300")
program.setBg("steel blue")

#Buttons
program.addButtons(["Bay One ON", "Bay One OFF"], ButtonHandler)
program.addButtons(["Bay Two ON", "Bay Two OFF"], ButtonHandler)
program.addButtons(["Bay Three ON", "Bay Three OFF"], ButtonHandler)
program.addButtons(["Bay Four ON", "Bay Four OFF"], ButtonHandler)
program.addButtons(["Bay Auto ON", "Bay Auto OFF"], ButtonHandler)
program.addButtons(["Changer ON", "Changer OFF"], ButtonHandler)


#POS
program.setSize("Fullscreen")




program.go()


