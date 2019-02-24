#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
#GPIO.output(18, False)
