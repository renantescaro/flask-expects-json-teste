import requests
import json
import sys
sys.path.append('/home/renan/Área de Trabalho/flask/flask-expects-json-teste/')
from flaskr.utils.debug import Debug


# passando todos os parametros obrigatórios
def test_requisicao_ok():
    headers = {'content-type':'application/json'}
    url     = 'http://localhost:5000/requisicao'
    data    =  json.dumps({
        'name'    : 'renan',
        'email'   : 'renan@tescaro.com',
        'password': '112233' })
    retorno = requests.post(url=url, data=data, headers=headers)
    assert retorno.status_code == 200


# não passando todos os parametros obrigatórios
def test_requisicao_erro():
    headers = {'content-type':'application/json'}
    url     = 'http://localhost:5000/requisicao'
    data    =  json.dumps({
        'name'    : 'renan',
        'password': '112233' })
    retorno = requests.post(url=url, data=data, headers=headers)
    assert retorno.status_code == 400