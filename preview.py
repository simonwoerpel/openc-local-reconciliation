import json
from config import PROPERTY_NAMES
from search.elastic import client


TMPL = """
<h3>{name}</h3>
<strong>Company id (OpenCorporates)</strong>: {company_number}<br>
<strong>Registered address:</strong> {registered_address}<br>
<strong>Status:</strong> {current_status}<br>
<strong>Jurisdiction code:</strong> {jurisdiction_code}<br>
<strong>Registered office (aka City):</strong> {registered_office}<br>
<strong>Native id (registrar + register type + id):</strong> {native_company_number}<br>
<strong>Registry ID:</strong> {_registerNummer}<br>
<strong>Registry:</strong> {_registerArt}</p>
"""


def render(hit):
    doc = {k: hit.get(k, hit.get('all_attributes', {}).get(k, '')) for k in PROPERTY_NAMES.keys()}
    return TMPL.format(data=json.dumps(doc), **doc)


def get_preview(id_):
    res = client.search(index='opencorporates', body={
        'query': {
            'term': {
                'company_number.keyword': id_
            }
        }
    })
    if res['hits']['total'] > 0:
        return render(res['hits']['hits'][0]['_source'])
