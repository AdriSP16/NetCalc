from flask import Flask, render_template, request, jsonify # type: ignore
from network_utils import calcular_red

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    ip = request.form.get("ip")
    mascara = request.form.get("mascara")
    export_json = request.form.get("json")

    resultado = calcular_red(ip, mascara)

    if export_json:
        return jsonify(resultado)
    
    return render_template("result.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
