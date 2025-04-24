from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify
import os
from network_utils import calcular_red
import json

# Inicializamos Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    ip = request.form.get("ip")
    mascara = request.form.get("mascara")
    export_json = request.form.get("json")

    try:
        if not ip:
            raise ValueError("La dirección IP es obligatoria.")

        resultado = calcular_red(ip, mascara)

        if export_json:
            # Guardamos el resultado en cookies para después usarlo en result.html
            response = make_response(render_template("download_redirect.html", resultado=resultado))
            response.set_cookie("resultado", json.dumps(resultado))  # Guardamos el resultado en cookies
            return response

        return render_template("result.html", resultado=resultado)

    except Exception as e:
        return render_template("index.html", error=str(e))

@app.route("/result", methods=["GET"])
def result():
    # Obtener el resultado desde las cookies
    resultado = request.cookies.get("resultado")
    if resultado:
        resultado = json.loads(resultado)
        return render_template("result.html", resultado=resultado)
    return redirect(url_for("index"))  # Si no hay resultado, redirige al inicio

def run_flask():
    """Inicia la aplicación Flask en modo servidor"""
    app.run(debug=True)

if __name__ == "__main__":
    run_flask()
