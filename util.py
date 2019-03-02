import json

from flask import current_app as app, request, jsonify


def jsonpify(func):
    """
    Like jsonify but wraps result in a JSONP callback if a 'callback'
    query param is supplied.
    """
    def inner(*args, **kwargs):
        data = func(*args, **kwargs)
        callback = request.args.get('callback')
        if callback:
            response = app.make_response('%s(%s)' % (callback, json.dumps(data)))
            response.mimetype = 'text/javascript'
            return response
        return jsonify(data)
    return inner


class DeprecatedException(Exception):
    pass
