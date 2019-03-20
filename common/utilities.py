import json
from jsonschema import validate, ValidationError
import logging

def is_valid_json(request_body):
    try:
        json_data = json.loads(request_body)
        return True
    except:
        return False

def is_valid_request_body(request_body, request_schema):
    try:
        validate(request_body, request_schema)
        return True
    except ValidationError:
        logging.debug("Request Body: {} failed validation.".format(request_body))
        return False

