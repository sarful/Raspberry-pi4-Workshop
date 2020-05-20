import Adafruit_DHT

dht_sensor=Adafruit_DHT.DHT11
dht_pin=21

while True:
    temp, humi =Adafruit_DHT.read_retry(dht_sensor,dht_pin)
    if temp is not None and humi is not None:
        print("temp={} C  and humi={} %".format(humi,temp))
        
    else:
        
        print("Sensor Not work")