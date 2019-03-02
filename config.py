METADATA = {
    'name': 'OpenCorporates DE Companies Reconciliation Service',
    'defaultTypes': [{'id': '/company', 'name': 'Company'}],
    'extend': {
        'propose_properties': {
            'service_url': 'http://localhost:5000',
            'service_path': '/propose_properties'
        },
        'property_settings': []
    },
    'preview': {
        'url': 'http://localhost:5000/preview?id={{id}}',
        'width': 300,
        'height': 300
    }
}

PROPERTIES = [{
    'id': 'name',
    'name': 'Name'
}, {
    'id': 'company_number',
    'name': 'Company id (OpenCorporates)'
}, {
    'id': 'registered_address',
    'name': 'Registered address'
}, {
    'id': 'current_status',
    'name': 'Status'
}, {
    'id': 'jurisdiction_code',
    'name': 'Jurisdiction code'
}, {
    'id': 'registered_office',
    'name': 'Registered office (aka City)'
}, {
    'id': 'native_company_number',
    'name': 'Native id (registrar + register type + id)'
}, {
    'id': '_registerNummer',
    'name': 'Registry ID'
}, {
    'id': '_registerArt',
    'name': 'Registry'
}]

PROPERTY_NAMES = {p['id']: p['name'] for p in PROPERTIES}

# Matching threshold.
MATCH_THRESHOLD = 10
