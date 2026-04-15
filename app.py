from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Habilitamos CORS para que tu React (que correrá en otro puerto) pueda pedirle datos a Flask sin bloqueos de seguridad
CORS(app) 

# Una ruta básica para comprobar que el servidor funciona
@app.route('/')
def home():
    return "¡El backend en Flask está vivo!"

# Este es el endpoint (ruta) que consumirá tu frontend de React
@app.route('/api/test', methods=['GET'])
def get_data():
    datos = {
        "mensaje": "¡Conexión exitosa!",
        "status": "success",
        "tecnologia": "Python/Flask"
    }
    # jsonify convierte nuestro diccionario de Python a un formato JSON que React entiende perfectamente
    return jsonify(datos)

if __name__ == '__main__':
    # debug=True hace que el servidor se reinicie automáticamente si guardas cambios en el código
    app.run(debug=True, port=5000)