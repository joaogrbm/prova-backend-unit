import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

receitas = [
    {
        "titulo": "Pipoca",
        "ingredientes": [
            "Milho",
            "Oleo",
            "Sal"
        ],
        "preparo" : "Jogue o milho com oleo na panela, ligue o forno e espere o "
                    "milho estourar. Adicione sal a gosto",
        "rendimento" : "2 porções"

    },
]

class Receitas(Resource):
    def get(self):
        return {'status': 200, 'data': receitas}

    def post(self):
        novaReceita = json.loads(request.data)
        receitas.append(novaReceita)
        return {
            "message": "Created!",
            "newValue": novaReceita
        }

class Receita(Resource):
    def get(self, indice):
        try:
            return receitas[indice]
        except IndexError:
            mensagem = "O índice {} não foi encontrado no array".format(indice)
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido"
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }

    def delete(self, indice):
        receitas.pop(indice)
        return {
            "message": "Deleted!",
            "arrayAtual": receitas
        }

    def put(self, indice):
        novoValor = json.loads(request.data)
        receitas[indice] = novoValor
        return {
            "message": "Updated!",
            "newValue": novoValor
        }


api.add_resource(Receitas, '/receitas/')
api.add_resource(Receita, '/receitas/<int:indice>')


if __name__ == '__main__':
    app.run(debug=True)



