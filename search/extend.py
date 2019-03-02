"""
data extension endpoint
"""

import json

from config import PROPERTY_NAMES
from .elastic import client


def parse_elastic_result(res, properties):
    for hit in res['hits']['hits']:
        data = hit['_source']
        yield data['company_number'], {p: [{'str': data.get(p)}] if data.get(p) else [{}] for p in properties}


def extend(payload):
    payload = json.loads(payload)
    ids = payload['ids']
    properties = [p['id'] for p in payload['properties']]
    res = client.search(index='opencorporates', body={
        'query': {
            'terms': {
                'company_number.keyword': ids
            }
        }
    })
    return {
        'rows': {k: data for k, data in parse_elastic_result(res, properties)},
        'meta': [{
            'id': p,
            'name': PROPERTY_NAMES[p]
        } for p in properties]
    }
