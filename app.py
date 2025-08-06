from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

print("Archivo .env cargado")

# Ejemplo: leer la variable DATABASE_URL
database_url = os.getenv("DATABASE_URL")
print("Conectando a la base de datos:", database_url)


from flask import Flask
from routes.example import example_bp

app = Flask(__name__)
app.register_blueprint(example_bp)

@app.route("/")
def home():
    return "Servidor Flask funcionando - WaveSound"

if __name__ == "__main__":
    app.run(debug=True)
