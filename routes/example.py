from flask import Blueprint

example_bp = Blueprint("example", __name__)

@example_bp.route("/api/saludo")
def saludo():
    return {"mensaje": "Hola desde WaveSound API"}
