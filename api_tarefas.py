from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = []


# listar todos
@app.route("/", methods=['GET'])
def all():
    return jsonify(tarefas)


# litar por id
@app.route("/<int:id>/", methods=['GET'])
def listar_registro(id):
    try:
        response = tarefas[id]
    except IndexError:
        msg = f'Registro {id} não existe'
        response = {"status": "erro", "mensagem": msg}
    return jsonify(response)


# inserir novo registro
@app.route("/insert/", methods=['POST'])
def insert():
    dados = json.loads(request.data)
    pos = len(tarefas)
    dados['id'] = pos
    tarefas.append(dados)
    return jsonify(tarefas[pos])


# atualizar somente status
@app.route("/update/<int:id>", methods=['PUT'])
def update(id):
    dados = json.loads(request.data)
    tarefas[id]["status"] = dados["status"]
    return jsonify(dados)


@app.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    tarefas.pop(id)
    return jsonify({"status": "sucesso",
                    "mensagem": "Registro deletado"})


if __name__ == '__main__':
    app.run(debug=True)
