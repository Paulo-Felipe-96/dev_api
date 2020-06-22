from flask import Flask, request
from flask_restful import Resource, Api
import json

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

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self):
        return desenvolvedores

    def delete(self):
        pass

    def put(self):
        pass

    def post(self):
        pass


class Pessoas(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'falha',
                        'mensagem': f'{id} não existe'}
        except BaseException:
            response = {'status': 'falha',
                        'mensagem': 'erro desconhecido'}
        return response

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso',
                'mensagem': f'{id} excluído com sucesso'}

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return {'status': 'sucesso',
                'mensagem': f'{id} atualizado'}


api.add_resource(Pessoas, '/<int:id>/')
api.add_resource(Pessoa, '/')

if __name__ == '__main__':
    app.run(debug=True)
