from flask_restful import reqparse


class InvalidUsage(Exception):
    def __init__(self, message, status_code=None, payload=None):
        print('JJconsole: ', message)
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code if status_code else 400
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class Validate(object):
    def getSpellcheckArgs(self, word):
        get_spell_check_args = reqparse.RequestParser()
        return get_spell_check_args.parse_args(strict=True)
