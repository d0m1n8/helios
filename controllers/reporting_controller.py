from flask import Blueprint, request, jsonify
from flask_api import status
import json
import logging
from common.utilities import is_valid_json, is_valid_request_body

reporting_controller = Blueprint("reporting", __name__)

@reporting_controller.route('/reporting', methods=['GET'])
def get_report():
    response = jsonify({'name': 'Ope', 'message': 'I love peace!'})
    response.status_code = 404
    return response
