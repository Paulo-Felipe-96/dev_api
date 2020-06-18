from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'id': 0,
        'nome': 'Paulo Martins',
        'habilidades':
            ['HTML5', 'CSS3', 'Javascript',
             'Nodejs', 'Express', 'Nunjucks', 'npm',
             'Python', 'Virtualenvs', 'Django', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Galleani',
        'habilidades': ['Python', 'Django']
    }
]


# recupera, altera e deleta um desenvolvedor pelo ID
@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            msg = f'ID {id} não existe'
            response = {'status': 'falha',
                        'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, fale com o administrador'
            response = {'status': 'erro',
                        'mensagem': msg}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


@app.route("/dev/", methods=['POST'])
def insert():
    dados = json.loads(request.data)
    pos = len(devs)
    dados['id'] = pos
    devs.append(dados)
    msg = 'Inserido com sucesso'
    return jsonify(devs[pos])


# devolve toods os desenvolvedores
@app.route("/dev/all/", methods=['GET'])
def allDevs():
    des = devs
    return jsonify(des)


if __name__ == '__main__':
    app.run(debug=True)
