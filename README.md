# openc-local-reconciliation

Serving a small [reconciliation
service](https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API)
for OpenRefine locally against an OpenCorporates dump. Of course there is the
great [OpenCorporates reconciliation service](https://opencorporates.com/reconcile)
available, but if you don't want to stress this endpoint with your huge
list of company names that you want to match, you can set up a local service
(which is much faster then.)

You can reconcile names against the companies in the OpenCorporates dump and
obtain extra data via the `/extend` endpoint:

`/propose_properties`

```json
  "properties": [
    {
      "id": "name",
      "name": "Name"
    },
    {
      "id": "company_number",
      "name": "Company id (OpenCorporates)"
    },
    {
      "id": "registered_address",
      "name": "Registered address"
    },
    {
      "id": "current_status",
      "name": "Status"
    },
    {
      "id": "jurisdiction_code",
      "name": "Jurisdiction code"
    },
    {
      "id": "registered_office",
      "name": "Registered office (aka City)"
    },
    {
      "id": "native_company_number",
      "name": "Native id (registrar + register type + id)"
    },
    {
      "id": "_registerNummer",
      "name": "Registry ID"
    },
    {
      "id": "_registerArt",
      "name": "Registry"
    }
  ]
```

## Prerequisites

You need a local elasticsearch instance filled with a OpenCorporates dump,
[like the german one you can get here](https://offeneregister.de/#download).

Download the "Line-delimited JSON" and feed it into Elasticsearch, e.g. via
[Logstash](https://www.elastic.co/products/logstash)

        cat de_companies.json | /path/to/logstash -f logstash.conf

That's enough, we don't need any index mapping.

## Run this app

Clone into somewhere:

        git clone git@github.com:simonwoerpel/openc-local-reconciliation.git

Install requirements for this app (use a virtual python environment):

        pip install -r requirements.txt

Then fire up this app via:

        FLASK_APP=app.py flask run

You will find the reconciliation endpoint at
[localhost:5000/reconcile](http://localhost:5000/reconcile)

Add this service in your reconciliation menu in OpenRefine (refer to their docs how to do that).

## TODO
- use proper settings management (see `config.py` for a start)
- make preview nicer
