from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = f'ID {id} não existe'
            response = {'status': 'falha',
                        'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, fale com o administrador'
            response = {'status': 'erro',
                        'mensagem': msg}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def post(self, id):
        pass

    def delete(self, id):
        try:
            desenvolvedores.pop(id)
        except IndexError:
            msg = 'Index inválido'
            return {'status': 'erro', 'mensagem': msg}
        except BaseException:
            return {'status': 'erro', 'mensagem': 'desconhecido'}
        else:
            msg = 'Registro deletado'
            return {'status': 'sucesso', 'mensagem': msg}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        pos = len(desenvolvedores)
        dados['id'] = pos
        desenvolvedores.append(dados)
        return desenvolvedores[pos]


# aqui, os resources são equivalentes as rotas
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)
