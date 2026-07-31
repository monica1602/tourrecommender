"""
Backend Flask para o site de recomendação de passeios turísticos.
"""
from flask import Flask, render_template, jsonify, request
from tour_data import get_paises, get_cidades, get_tipos, recomendar_passeios

app = Flask(__name__, static_folder="static", template_folder="static")


@app.route("/")
def index():
    """Serve a página principal."""
    return render_template("index.html")


@app.route("/api/paises")
def api_paises():
    """Retorna lista de países disponíveis."""
    return jsonify(get_paises())


@app.route("/api/cidades")
def api_cidades():
    """Retorna cidades filtradas por país (opcional)."""
    pais = request.args.get("pais", None)
    return jsonify(get_cidades(pais))


@app.route("/api/tipos")
def api_tipos():
    """Retorna tipos de passeio disponíveis."""
    return jsonify(get_tipos())


@app.route("/api/recomendar", methods=["POST"])
def api_recomendar():
    """Recebe filtros e retorna passeios recomendados."""
    dados = request.get_json()

    filtros = {
        "pais": dados.get("pais", ""),
        "cidade": dados.get("cidade", ""),
        "tipo": dados.get("tipo", ""),
        "gratuito": dados.get("gratuito", False),
        "preco_max": dados.get("preco_max", 0),
        "duracao_max": dados.get("duracao_max", 0),
        "pessoas": dados.get("pessoas", 0),
    }

    resultados = recomendar_passeios(filtros)

    return jsonify({
        "total": len(resultados),
        "passeios": resultados
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
