from flask import Blueprint, request, jsonify
from flask_api import status
import json
import logging as logger
from common.utilities import is_valid_json, is_valid_request_body
from urllib.request import Request, urlopen
from models.jobs import JobObject, JobStore
job_controller = Blueprint("job", __name__)

job_store = JobStore("jobs")


@job_controller.route('/job', methods=['POST'])
def add_job():
    job_request = request.json
    response = job_store.insert_one(job_request['name'], job_request['link'], job_request['frequency'])
    return json.dumps(response), 200


@job_controller.route('/job/<id>', methods=['GET'])
def get_job(id):
    response = job_store.find_by_id(id)
    return json.dumps(response), 200

@job_controller.route('/job', methods=['GET'])
def get_all_job():
    response = job_store.find_all_jobs()
    return json.dumps(response), 200



@job_controller.route('/job', methods=['PUT'])
def edit_job():
    return "notification", 200


@job_controller.route('/job', methods=['DELETE'])
def delete_job():
    return "notification", 200
