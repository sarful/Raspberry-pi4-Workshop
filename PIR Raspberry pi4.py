import RPi.GPIO as GPIO
import time

sensor = 24
buzzer = 20
relay=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(relay,GPIO.OUT)

print ("Initialzing PIR Sensor......")
time.sleep(5)
print ("PIR Ready...")
print (" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          GPIO.output(relay,True)
          print ("Motion Detected")
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)
          GPIO.output(relay,False)
          print ("Motion Not Detected")



except KeyboardInterrupt:
    GPIO.cleanup()