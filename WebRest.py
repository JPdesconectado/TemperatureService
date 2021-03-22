from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for, abort
from flask_httpauth import HTTPBasicAuth
from Dados import Dados

auth = HTTPBasicAuth()
app = Flask(__name__)

info = Dados()
lista = info.selectAll()
dados = []
for l in lista:
    dado = {
            'idinfo': l[0],
            'temperature': l[1],
            'moisture': l[2],
            'luminosity': l[3],
            'date': l[4],
            'hour': l[5]
            }
            
    dados.append(dado)


@app.route('/dados', methods=['GET'])
def obtem_dados():
    dados.clear()
    lista = info.selectAll()
    for l in lista:
        dado = {
                'idinfo': l[0],
                'temperature': l[1],
                'moisture': l[2],
                'luminosity': l[3],
                'date': l[4],
                'hour': l[5]
                }
                
        dados.append(dado)
    return jsonify({'dados': dados})


@app.route('/dados/<int:idDado>', methods=['GET'])
def detalhe_dado(idDado):
    resultado = [resultado for resultado in dados if resultado['idinfo'] == idDado]
    if len(resultado) == 0:
        abort(404)
    return jsonify({'dados': resultado})


@app.route('/dados/<int:id>', methods=['DELETE'])
def excluir_dados(id):
    resultado = [resultado for resultado in dados if resultado['id'] == id]
    if len(resultado) == 0:
        abort(404)
    dados.remove(resultado[0])
    return jsonify({'resultado': True})


@app.route('/dados', methods=['POST'])
def criar_dados():
    if not request.json or not 'temperature' in request.json:
        abort(400)
    dado = {

        'temperature': request.json['temperature'],
        'moisture': request.json.get('moisture', ""),
        'luminosity': request.json.get('luminosity', ""),
        'date': request.json.get('date', ""),
        'hour': request.json.get('hour', "")
    }
    info.temperature = dado['temperature']
    info.moisture = dado['moisture']
    info.luminosity = dado['luminosity']
    info.date = dado['date']
    info.hour = dado['hour']
    teste = info.insertDate()
    dados.append(dado)
    return jsonify({'dado': dado}), 201

# tentar acessar recurso que não existe
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'erro': 'Recurso Nao encontrado'}), 404)

if __name__ == "__main__":
    print('Servidor executando...')
    app.run(debug=True)