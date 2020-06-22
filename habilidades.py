from flask_restful import Resource
from flask import Flask, request
import json

habilidades = ['Python', 'Java', 'Flask', 'PHP']


class Habilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        try:
            dados = json.loads(request.data)
        except BaseException:
            return {'status': 'erro', 'mensagem': 'desconhecido'}
        else:
            habilidades.append(dados)
            return {'status': 'sucesso', 'mensagem': 'habilidade inserida'}


class ManipulaHabilidades(Resource):
    def delete(self, id):
        try:
            habilidades.pop(id)
            response = {'status': 'sucesso',
                        'mensagem': 'registro deletado'}
        except IndexError:
            response = {'status': 'erro',
                        'mensagem': f'Index {id} não existe'}
        except BaseException:
            response = {'status': 'erro',
                        'mensagem': 'desconhecido'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        try:
            habilidades[id] = dados
            response = {'status': 'sucesso',
                        'mensagem': 'registro atualizado'}
        except IndexError:
            response = {'status': 'erro',
                        'mensagem': f'Index {id} não existe'}
        except BaseException:
            response = {'status': 'erro',
                        'mensagem': 'desconhecido'}
        return response
