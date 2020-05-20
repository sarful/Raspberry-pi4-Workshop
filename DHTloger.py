import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21

while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(DHT_PIN, DHT_SENSOR)

    if humidity is not None and temperature is not None:
        print("Temp={} C  Humidity={}%".format(temperature, humidity))
        
    else:
        print("Failed to retrieve data from humidity sensor")
