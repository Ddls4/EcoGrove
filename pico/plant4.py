import dht
from machine import Pin, ADC
import time

sensor_dht = dht.DHT11(Pin(0)) # pwm
sensortierra = ADC(Pin(26)) #ADC
relay = Pin(2 , Pin.OUT)


def plantaTH():
    # DHT
    sensor_dht.measure()
    T = sensor_dht.temperature()
    H = sensor_dht.humidity()
    
    #Humedad en tierra
    sensorHumedadTierra = sensortierra.read_u16() 
    
    
    
    humedad_tierra = (63000 - sensorHumedadTierra)/63000 * 100
    
    print("Humedad en tierra: ",humedad_tierra)
    print("sesor", sensorHumedadTierra)
    print("Temperatura: ",T)
    print("Humedad: ",H)
    
    if ( sensorHumedadTierra < 0 ):
        relay.value(0)
        time.sleep(2)
    else:
        relay.value(1)
        time.sleep(2)
      
    time.sleep(1)
    
