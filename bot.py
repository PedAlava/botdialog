import requests  
import os
from flask import Flask, request
import extracmodelo
#import asistente
#BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable


app = Flask(__name__)


@app.route('/me', methods=['POST'])
def main():  
    data = request.json
    parametro = data['queryResult']['parameters']['modelos']
    print(parametro)
    response = extracmodelo.modelo(parametro)
    nombre ,precio ,url,sitio = extracmodelo.mensaTelegram(parametro)
    subtitulo = "Modelo: " + nombre +" Precio: "+ precio
    if sitio == "store":
        mensaj = "Visualiza algun producto de tu interes"
    else:
        mensaj = "Visualiza tu "+ nombre +" y añadelo al carrito si deseas."
    sitio = "https://tecno-store2.herokuapp.com/" +sitio
    if response is not None:
        json_data = {
            
    "richContent": [
        [
         {
        "type": "image",
        "rawUrl": url,
        "accessibilityText": "Producto"
      },
      {
        "type": "info",
        "title": nombre,
        "subtitle": subtitulo,
        "actionLink": sitio
      },
      {
        "type": "chips",
        "options": [
          {
            "text": mensaj,
            "link": sitio
          },
          {
            "text": "Visualizar mas productos",
            "link": "https://tecno-store2.herokuapp.com/store"
          }
        ]
      }
        ]
    ]

     }
    else:
        json_data = {
            "fulfillmentText": response,"buttons":[ { 
                "text": "debe",
                "postback": "dffdsf"
                    }
                ]
        }
    return json_data


if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
