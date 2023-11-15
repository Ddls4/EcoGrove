from flask import Flask, render_template, request
from flask_mqtt import Mqtt

app = Flask(__name__)
# Configuracion de MQTT
app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app, connect_async=True)

@app.route('/')
def index():
    return render_template("index.hbs")
@app.route('/en')
def Español():
    return render_template('index_EN.html')

@app.route("/slider", methods=["POST"])
def slider():
    # Obtener el valor del slider
    value = request.form.get("value")
    print(value)

    return "El valor del slider se publicó correctamente"
@app.route("/slider2", methods=["POST"])
def slider():
    # Obtener el valor del slider
    value = request.form.get("value2")
    print(value)

    return "El valor del slider se publicó correctamente"

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('luces')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

if __name__  == "__main__":
    app.run(host='0.0.0.0',debug=True,port=4000)
