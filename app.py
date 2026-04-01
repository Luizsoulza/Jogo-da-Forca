from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.jogo_forca import JogoForca

app = Flask(__name__)
CORS(app)
jogo = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categorias', methods=['GET'])
def categorias():
    temp = JogoForca.__new__(JogoForca)
    temp.banco_palavras = __import__('src.banco_palavras', fromlist=['BancoPalavras']).BancoPalavras()
    return jsonify(temp.banco_palavras.listar_categorias())

@app.route('/iniciar', methods=['POST'])
def iniciar():
    global jogo
    dados = request.get_json()
    categoria = dados.get('categoria')
    jogo = JogoForca(categoria)
    return jsonify(jogo.obter_estado_completo())

@app.route('/tentar-letra', methods=['POST'])
def tentar_letra():
    global jogo

    # CORRIGIDO: verifica se o jogo foi iniciado antes de tentar uma letra
    if jogo is None:
        return jsonify({"erro": "Jogo não iniciado. Chame /iniciar primeiro."}), 400

    dados = request.get_json()
    letra = dados.get('letra')

    try:
        jogo.tentar_letra(letra)
        return jsonify(jogo.obter_estado_completo())
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@app.route('/estado', methods=['GET'])
def estado():
    # CORRIGIDO: verifica se o jogo foi iniciado antes de retornar estado
    if jogo is None:
        return jsonify({"erro": "Jogo não iniciado."}), 400
    return jsonify(jogo.obter_estado_completo())

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global jogo

    # CORRIGIDO: verifica se o jogo existe antes de reiniciar
    if jogo is None:
        return jsonify({"erro": "Jogo não iniciado."}), 400

    dados = request.get_json()
    categoria = dados.get('categoria')
    jogo.reiniciar_jogo(categoria)
    return jsonify(jogo.obter_estado_completo())

if __name__ == '__main__':
    app.run(debug=True)