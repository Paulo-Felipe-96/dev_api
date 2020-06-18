from flask import Flask, jsonify, request
import json

app = Flask(__name__)

pessoas = [
    {
        "id": 0,
        "status": "ativo",
        "nome": "Paulo",
        "habilidades": [
            "Javascript",
            "Nodejs",
            "HTML5",
            "Nunjucks",
            "Express",
            "Python",
            "Django",
            "Flask"
        ]
    }
]


# retorna todos
@app.route("/", methods=["GET"])
def returnall():
    return jsonify(pessoas)


# retorna por ID
@app.route("/<int:id>", methods=["GET"])
def returnbyid(id):
    try:
        response = pessoas[id]
    except IndexError:
        msg = f"ID {id} não existe"
        response = {"status": "erro", "mensagem": msg}
    return jsonify(response)


# atualiza registro
@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    dados = json.loads(request.data)
    try:
        pessoas[id]["status"] = dados["status"]
    except IndexError:
        msg = f'ID {id} não existe'
        return jsonify({"status": "erro", "mensagem": msg})
    else:
        return jsonify(dados)


# insere registro
@app.route("/insert/", methods=["POST"])
def insert():
    dados = json.loads(request.data)
    pos = len(pessoas)
    dados["id"] = pos
    pessoas.append(dados)
    return jsonify(dados)


# deleta registro
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        pessoas.pop(id)
        msg = f'Registro {id} deletado'
    except IndexError:
        msg = f'Registro {id} não existe'
        return jsonify({"status": "erro", "mensagem": msg})
    else:
        return jsonify({"status": "sucesso", "mensagem": msg})


if __name__ == '__main__':
    app.run()
