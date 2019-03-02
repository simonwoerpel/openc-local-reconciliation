"""
Simple OpenCorporates reconciliation service for use against a local Elasticsearch index

See http://code.google.com/p/google-refine/wiki/ReconciliationServiceApi.
"""

import os
from flask import Flask

import api


app = Flask(__name__)
app.debug = os.environ.get('FLASK_DEBUG', None) == '1'


@app.route('/propose_properties', methods=['GET'])
def propose_properties():
    return api.propose_properties()


@app.route('/reconcile', methods=['POST', 'GET'])
def reconcile():
    return api.reconcile()


@app.route('/preview', methods=['GET'])
def preview():
    return api.preview()
