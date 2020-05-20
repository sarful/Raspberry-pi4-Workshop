import RPi.GPIO as GPIO
import time

led=21
button=20
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button,GPIO.IN)

while True:
    
    num =GPIO.input(button)
    print(num)
    if (num==1):
        
        
        GPIO.output(led,GPIO.HIGH)
        
    else:
        
        GPIO.output(led,GPIO.LOW)
        
        
