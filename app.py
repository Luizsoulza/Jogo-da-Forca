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
    dados = request.get_json()
    letra = dados.get('letra')
    jogo.tentar_letra(letra)
    return jsonify(jogo.obter_estado_completo())

@app.route('/estado', methods=['GET'])
def estado():
    return jsonify(jogo.obter_estado_completo())

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global jogo
    dados = request.get_json()
    categoria = dados.get('categoria')
    jogo.reiniciar_jogo(categoria)
    return jsonify(jogo.obter_estado_completo())

if __name__ == '__main__':
    app.run(debug=True)