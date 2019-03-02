"""
api endpoints
"""

import json
from flask import request

from config import METADATA, PROPERTIES
from preview import get_preview
from search.base import search
from search.extend import extend
from util import jsonpify, DeprecatedException


@jsonpify
def propose_properties():
    type_ = request.form.get('type')
    limit = request.form.get('limit')
    return {
        'properties': PROPERTIES,
        'type': type_ or '/company',
        'limit': limit
    }


@jsonpify
def reconcile():
    # single query mode is deprecated:
    # https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API#deprecated-single-query-mode
    if request.form.get('query'):
        raise DeprecatedException('Single query endpoint is deprecated in recent version of OpenRefine.')

    # If a 'queries' parameter is supplied then it is a dictionary
    # of (key, query) pairs representing a batch of queries. We
    # should return a dictionary of (key, results) pairs.
    queries = request.form.get('queries')
    if queries:
        queries = json.loads(queries)
        results = {}
        for (key, query) in queries.items():
            results[key] = {'result': search(query['query'])}
        return results

    # data extension
    extend_payload = request.form.get('extend')
    if extend_payload:
        return extend(extend_payload)

    # If neither a 'query' nor 'queries' parameter is supplied then
    # we should return the service metadata.
    return METADATA


# @jsonpify
# def suggest():
#     prefix = request.form.get('prefix')
#     if prefix:
#         return


def preview():
    if 'id' in request.args:
        return get_preview(request.args['id'])
    return 'no preview'
