from appJar import *
import RPi.GPIO as GPIO
import time

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT) #Bay One
GPIO.setup(15, GPIO.OUT) #Bay Two / Three
GPIO.setup(16, GPIO.OUT) #Front / Back / Bay Four
GPIO.setup(18, GPIO.OUT) #Bay Five / Six

#GPIO Startup State
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)


def ButtonHandler(select):
    if select == "Bay One ON":
        GPIO.output(13, GPIO.LOW)
        program.infoBox("Message","Bay One Siren ON")
    elif select == "Bay One OFF":
        GPIO.output(13, GPIO.HIGH)
        program.infoBox("Message","Bay One Siren OFF")
    elif select == "Bay Two / Three ON":
        GPIO.output(15, GPIO.LOW)
        program.infoBox("Message","Bay Two / Three Siren ON")
    elif select == "Bay Two / Three OFF":
        GPIO.output(15, GPIO.HIGH)
        program.infoBox("Message","Bay Two / Three Siren OFF")
    elif select == "Bay Four / Front / Back ON":
        GPIO.output(16, GPIO.LOW)
        program.infoBox("Message","Bay Four / Front / Back Siren ON")
    elif select == "Bay Four / Front / Back OFF":
        GPIO.output(16, GPIO.HIGH)
        program.infoBox("Message","Bay Four / Front / Back Siren OFF")
    elif select == "Bay Five / Six ON":
        GPIO.output(18, GPIO.LOW)
        program.infoBox("Message","Bay Five / Six Siren ON")
    elif select == "Bay Five / Six OFF":
        GPIO.output(18, GPIO.HIGH)
        program.infoBox("Message","Bay Five / Six Siren OFF")


#Style
program = gui("Title", "500x300")
program.setBg("white")
program.addLabel("title", "44th")
program.setLabelFg("title", "black")

#Buttons
program.addButtons(["Bay One ON", "Bay One OFF"], ButtonHandler)
program.addButtons(["Bay Two / Three ON", "Bay Two / Three OFF"], ButtonHandler)
program.addButtons(["Bay Four / Front / Back ON", "Bay Four / Front / Back OFF"], ButtonHandler)
program.addButtons(["Bay Five / Six ON", "Bay Five / Six OFF"], ButtonHandler)


#POS
program.setSize("Fullscreen")


program.go()

GPIO.cleanup()