from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os

# 1. Le decimos a Flask que su carpeta de vistas y archivos estáticos será 'dist'
app = Flask(__name__, 
            static_folder='dist/assets', 
            template_folder='dist')

CORS(app)

# --- RUTAS DE LA API (Backend Pecu) ---
@app.route('/api/test', methods=['GET'])
def get_data():
    datos = {
        "mensaje": "¡Conexión exitosa!",
        "status": "success",
        "tecnologia": "Python/Flask"
    }
    return jsonify(datos)

# --- RUTAS DE REACT (Frontend) ---

# 2. Cuando entren a la URL principal, Flask muestra tu frontend
@app.route('/')
def serve_react():
    return render_template('index.html')

# 3. Este "Catch-all" es vital. Permite que tus rutas de React (como /login o /registro-animal) 
# funcionen correctamente si el usuario recarga la página.
@app.route('/<path:path>')
def catch_all(path):
    # Si están pidiendo un archivo que existe (como un logo o imagen), se lo mandamos
    if os.path.exists(os.path.join(app.template_folder, path)):
        return send_from_directory(app.template_folder, path)
    
    # Si la ruta no es un archivo ni una ruta de la API, dejamos que React Router se encargue
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)