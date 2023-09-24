#pip install Flask
#Ctrl+S - Guadar / Ctrl+Ñ - cmd / CTRL+C

from flask import Flask, render_template
import random
servidor = Flask(__name__)

def rand():
    global humedad
    global Temperatura
    humedad = random.randrange(50,80)
    Temperatura = random.randrange(0,40) 
    
#   inciar la pagina principal 
@servidor.route("/")
def inicio():
    rand()
    return render_template("index.hbs",humedad=humedad,Temperatura=Temperatura)
#   Pagina para logear
@servidor.route('/en')
def Español():
    return render_template('index_EN.html')

if __name__  == "__main__":
    servidor.run(host='0.0.0.0',debug=True,port=4000)
