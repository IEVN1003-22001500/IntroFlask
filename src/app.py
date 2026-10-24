
from flask import Flask, jsonify, request, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS

from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp

from config import config

app = Flask(__name__)

# Configuración de la base de datos
app.config.from_object(config['development'])

# Conexión a MySQL
con = MySQL(app)

# Habilitar CORS
CORS(app)


# Registrar Blueprints
app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)


# Página no encontrada
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.run(debug=True)
