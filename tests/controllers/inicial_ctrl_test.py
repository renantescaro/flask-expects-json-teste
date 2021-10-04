import requests
import json
import sys


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


def test_requisicao_erro_limite_caracter():
    headers = {'content-type':'application/json'}
    url     = 'http://localhost:5000/requisicao'
    data    =  json.dumps({
        'name'    : 'renan teste caracteres',
        'email'   : 'renan@tescaro.com',
        'password': '112233' })
    retorno = requests.post(url=url, data=data, headers=headers)
    assert retorno.status_code == 400


# não passando todos os parametros obrigatórios
def test_requisicao_erro():
    headers = {'content-type':'application/json'}
    url     = 'http://localhost:5000/requisicao'
    data    =  json.dumps({
        'name'    : 'renan',
        'password': '112233' })
    retorno = requests.post(url=url, data=data, headers=headers)
    assert retorno.status_code == 400


# teste com type number
def test_requisicao_com_numero_ok():
    headers = {'content-type':'application/json'}
    url     = 'http://localhost:5000/requisicao'
    data    =  json.dumps({
        'idade'   : 1,
        'email'   : 'renan@tescaro.com',
        'password': '112233' })
    retorno = requests.post(url=url, data=data, headers=headers)
    assert retorno.status_code == 200


# teste com type number, passando string
def test_requisicao_com_numero_erro():
    headers = {'content-type':'application/json'}
    url     = 'http://localhost:5000/requisicao'
    data    =  json.dumps({
        'idade'   : '1',
        'email'   : 'renan@tescaro.com',
        'password': '112233' })
    retorno = requests.post(url=url, data=data, headers=headers)
    assert retorno.status_code == 400