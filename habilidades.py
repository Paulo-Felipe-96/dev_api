from flask_restful import Resource

habilidades = ['Python', 'Java', 'Flask', 'PHP']


class Habilidades(Resource):
    def get(self):
        return habilidades
