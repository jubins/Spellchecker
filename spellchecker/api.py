from flask import Flask, jsonify
from flask_restful import Api, Resource

from validators import Validate, InvalidUsage
from models import SpellCheck

app = Flask(__name__)


class Home(Resource):
    def get(self):
        response = {"message": "Welcome to the Spellchecker API! Go to /spellchecker/{word} to spellcheck."}
        return response


class Spellchecker(Resource):
    def get(self, word):
        args = Validate().getSpellcheckArgs(word)
        sc = SpellCheck()
        word_found, suggestions = sc.run(word)
        response = {"suggestions": suggestions,
                    "correct": word_found
                    }
        if not word_found and not suggestions:
            response = {'message': f'Word: {word} not found.', 'status_code': 404}

        return response

    @app.errorhandler(InvalidUsage)
    def handle_word_not_found(self, error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


api = Api(app)
api.add_resource(Home, '/')
api.add_resource(Spellchecker, '/spellcheck/<string:word>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31337, debug=True)
