import json
from flask import jsonify, render_template, Blueprint, make_response
from flask_expects_json import expects_json
from jsonschema import ValidationError

bp = Blueprint(
    'inical',
    __name__,
    template_folder='templates' )


class InicialCtrl:
    @bp.route('/', methods=['GET'])
    def inicial_template():
        return render_template(
            'inicial.html',
            titulo = 'inicial' )


    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'email': {'type': 'string'},
            'password': {'type': 'string'}
        },
        'required': ['email', 'password']
    }
    @bp.route('/requisicao', methods=['POST'])
    @expects_json(schema)
    def requisicao():
        return json.dumps({'status':True})


    @bp.errorhandler(400)
    def erro(error):
        if isinstance(error.description, ValidationError):
            original_error = error.description
            return make_response(
                jsonify({
                    'status'   : False,
                    'mensagem' : original_error.message}
                ), 400)
        return error