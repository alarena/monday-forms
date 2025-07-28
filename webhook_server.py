# webhook_server.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "¡Servidor Flask funcionando! Esperando webhooks de Monday.com.", 200

@app.route('/webhook', methods=['POST'])
def monday_webhook():
    if request.method == 'POST':
        data = request.json
        print("--- Webhook recibido de Monday.com ---")
        print(data)
      
        print("---------------------------------------")
        return "Webhook procesado correctamente", 200
    return "Método no permitido", 405

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
