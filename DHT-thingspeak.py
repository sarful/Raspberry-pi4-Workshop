import Adafruit_DHT
from time import time, sleep
from urllib.request import urlopen
import sys


WRITE_API = "2ZDBD2B17MUMA3XO" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)

SENSOR_PIN = 21
SENSOR_TYPE = Adafruit_DHT.DHT11

SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds


try:
    while True:
        
        if time() - SensorPrevSec > SensorInterval:
            SensorPrevSec = time()
            
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
            print("Humidity = {}%\tTemperature = {}C".format(humidity, temperature))
        
        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + "&field1={}&field2={}".format(temperature, humidity)
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            
            
            sleep(1)
            
except KeyboardInterrupt:
    conn.close()