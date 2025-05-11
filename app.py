from flask import Flask, request, jsonify, render_template
import json
import requests

app = Flask(__name__)

ARQUIVO = 'data.json'

def ler_time():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_time(time):
    with open(ARQUIVO, 'w') as f:
        json.dump(time, f, indent=4)

@app.route('/time', methods=['GET'])
def ver_time():
    time = ler_time()
    print("GET /time")
    return jsonify(time)

@app.route('/time', methods=['POST'])
def adicionar_pokemon():
    dados = request.json
    nome = dados.get("nome", "").lower()

    if not nome:
        return jsonify({"erro": "Você precisa informar o nome do Pokémon."}), 400

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}")

    if resposta.status_code != 200:
        return jsonify({"erro": "Pokémon não encontrado na PokéAPI."}), 404

    dados_pokeapi = resposta.json()
    tipo = dados_pokeapi['types'][0]['type']['name']
    imagem = dados_pokeapi['sprites']['front_default']
    nivel = 5  # valor padrão

    novo_pokemon = {
        "id": None, 
        "nome": nome.capitalize(),
        "tipo": tipo.capitalize(),
        "nivel": nivel,
        "imagem": imagem
    }

    time = ler_time()

    if len(time) >= 6:
        return jsonify({"erro": "O time já tem 6 Pokémons!"}), 400

    novo_pokemon["id"] = len(time) + 1
    time.append(novo_pokemon)
    salvar_time(time)

    print("POST /time:", novo_pokemon)
    return jsonify(novo_pokemon), 201

@app.route('/time/<int:id>', methods=['DELETE'])
def remover_pokemon(id):
    time = ler_time()
    novo_time = [p for p in time if p['id'] != id]

    if len(time) == len(novo_time):
        return jsonify({"erro": "Pokémon não encontrado!"}), 404

    for idx, poke in enumerate(novo_time, start=1):
        poke["id"] = idx

    salvar_time(novo_time)

    print(f"DELETE /time/{id}")
    return jsonify({"mensagem": "Pokémon removido!"})

@app.route('/visu')
def ver_html():
    time = ler_time()
    return render_template("time.html", time=time)

if __name__ == '__main__':
    app.run(debug=True)