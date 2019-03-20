from flask import Blueprint, request, jsonify
from flask_api import status
import json
import logging
from common.utilities import is_valid_json, is_valid_request_body

notification_controller = Blueprint("notification", __name__)

@notification_controller.route('/notifications', methods=['GET'])
def get_notification():
    return "notification", 200

@notification_controller.route('/notifications', methods=['POST'])
def add_notification():
    return json.dumps(request.json), 200

@notification_controller.route('/notifications', methods=['DELETE'])
def delete_notification():
    return "notification", 200

@notification_controller.route('/notifications', methods=['PUT'])
def edit_notification():
    return "notification", 200
