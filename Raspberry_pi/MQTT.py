# Librerias
import paho.mqtt.client as mqtt
import time

# Config de MQTT
broker = "test.mosquitto.org"
port = 1883
topic = "Python"

# MQTT
def on_message(client, userdata, msg):
    print("Mensaje recivido:")
    print(f"Topic: [{msg.topic}] Msg: {msg.payload}") 
    if msg.topic == "farm":
        if msg.payload == b'si':
            time.sleep(5)
            client.publish("farm", payload="no", qos=0, retain=False)
        elif msg.payload == b'no':
            print("chau")
    

# Crear el cliente
client = mqtt.Client("mqtt-test")
client.on_message = on_message
# Conectar al broker
client.connect(broker, port)
# Subscribe
client.subscribe(topic)
client.subscribe("farm") # si / no
client.subscribe("Ench") # si / no

client.loop_forever()