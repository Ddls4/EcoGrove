from umqtt import simple
import network
from time import sleep
from usario_contra import usuario
from usario_contra import contra
import plant4

from time import sleep

ssid = usuario
contra = contra

def conectarmqtt():
    global client
    # IP de la pc con flask
    client = simple.MQTTClient("Rasp", "192.168.0.100",1883)
    print(client.connect())
    if client.connect()==0:
        print("Conectado al broker")
        client.set_callback(sub_cb)
        client.subscribe("luces")
        # Detectar los mensajes
        while True:
            plant4.plantaTH()
            if True:
                client.wait_msg()
            else:
                client.check_msg()
                time.sleep(1)

              
            
def sub_cb(topic, msg):
    print((topic, msg))
    if msg == "encendido":
        estado_led = "encendido"
        cliente_pub("luces", estado_led)
    elif msg == "apagado":
        estado_led = "apagado"
        cliente_pub("luces", estado_led)
    sleep(1)
        
                       
def cliente_pub(nombre,valor):
    cliente.publish(nombre,valor)
     
def conectarse():
    red = network.WLAN(network.STA_IF)
    red.active(True)
    red.connect(ssid,contra)
    print("conectado")
    while red.isconnected()==False:
        print(" .", end=" ")
        sleep(0.5)
        if red.isconnected()==True:
            break
    print("Conexión Exitosa")
    print('Network config:', red.ifconfig(  ))
