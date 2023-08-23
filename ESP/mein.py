import dht
from machine import Pin, ADC
import time

sensor_dht = dht.DHT11(Pin(4))
sensor_tierra = ADC(0)
relay = Pin(5, Pin.OUT)

while True:
    # DHT
    sensor_dht.measure()
    T=sensor_dht.temperature()
    Humedad=sensor_dht.humidity()
    # Humedad en tierra
    sensor_humedad_tierra = sensor_tierra.read() 
    Humedad_tierra = (1023 - sensor_humedad_tierra )/1023 * 100
    
    print("Humedad en Tierra: ",Humedad_tierra)
    print("Temperatura: ",T)
    print("Humedad: ",Humedad)
    
    if ( Humedad_tierra < 0 ):
        time.sleep(2)
        relay.value(0)
    else:
        time.sleep(2)
        relay.value(1)
        
    time.sleep(1)
    
    
