from flask import Blueprint, request, jsonify
from flask_api import status
import json
import logging as logger
from common.utilities import is_valid_json, is_valid_request_body
from urllib.request import Request, urlopen

third_party_controller = Blueprint("third_party", __name__)


@third_party_controller.route("/third_party/register", methods=["POST"])
def registration():
    logger.info("state id object [{}]".format(request.data))
    return jsonify({"success": True, "message": "User Registered successfully"})

@third_party_controller.route("/third_party/register_bulk", methods=["POST"])
def bulkRegistration():
    logger.info("state id object [{}]".format(request.data))
    return jsonify({"success": True, "message": "Users Registered successfully"})

@third_party_controller.route("/third_party/attendance", methods=["POST"])
def attendance():
    logger.info("attendance object [{}]".format(request.data))
    return jsonify({"success": True, "message": "Successfully logged"})

@third_party_controller.route("/third_party/attendance_bulk", methods=["POST"])
def attendanceBulk():
    logger.info("attendance parameters [{}]".format(request.data))
    return jsonify({"status": True, "message": "Successfully logged"})

@third_party_controller.route("/third_party/get_logs", methods=["GET"])
def get_logs():
    logger.info("Pagination parameters [{}]".format(request.args["page"]))
    return jsonify({"content": [{"firstName": "Opeyemi", "userId": "123"},{"firstName": "Damilola", "userId": "12345"}]})

@third_party_controller.route("/third_party/get_log/<int:id>", methods=["GET"])
def get_log(id):
    logger.info("id that was returned [{}]".format(id))
    return jsonify({})
    pass
