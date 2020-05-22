import RPi.GPIO as GPIO
import time
import requests

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
          requests.post('https://maker.ifttt.com/trigger/Motion_Detector/with/key/nSnY012ZcVDsjlKHkdUymDC-Q1pTdsLGie2mvp9gw5I', params={"value1":"Call on your Emergeancy","value2":"8787878","value3":"none"})
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)
          GPIO.output(relay,False)
          print ("Motion Not Detected")



except KeyboardInterrupt:
    GPIO.cleanup()
