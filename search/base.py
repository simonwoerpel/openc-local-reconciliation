from config import MATCH_THRESHOLD
from .elastic import client


def search(query):

    # Initialize matches.
    matches = []

    res = client.search(index='opencorporates', body={
        'query': {
            'bool': {
                'should': [
                    {'match': {'name': query}},
                    {'match': {'previous_names.company_name': query}},
                ]
            }
        }
    })
    records = res['hits']['hits']

    # Search person records for matches.
    for r in records:
        data = r['_source']
        name = data['name']
        score = r['_score']

        if score > MATCH_THRESHOLD:
            matches.append({
                'id': data['company_number'],
                'name': data['name'],
                'score': score,
                'match': query == name,
                'type': [{'id': '/company', 'name': 'Company'}]
            })

    return matches
