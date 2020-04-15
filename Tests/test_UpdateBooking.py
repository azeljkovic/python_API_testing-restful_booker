import requests
import endpoints
import json
from pathlib import Path
import data
from fixtures import get_token


def testUpdateBookingValid(get_token):
    token = get_token
    headers = {'content-type': 'application/json', 'Cookie': token}
    file_request = Path('../JSON/request_update_valid.json')
    file_response = Path('../JSON/response_update_valid.json')
    with open(file_request) as f:
        payload = json.load(f)
    with open(file_response) as f:
        expected_response = json.load(f)

    try:
        r = requests.put(endpoints.Booking + '/' + data.valid_id, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    assert r.status_code == data.OK  # check the status code
    assert response == expected_response  # check the response


def testUpdateBookingInvalidID(get_token):
    token = get_token
    headers = {'content-type': 'application/json', 'Cookie': token}
    file_request = Path('../JSON/request_update_valid.json')
    with open(file_request) as f:
        payload = json.load(f)

    try:
        r = requests.put(endpoints.Booking + '/' + data.invalid_id, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.NOT_FOUND  # check the status code


def testUpdateBookingEmptyRequest(get_token):
    token = get_token
    headers = {'content-type': 'application/json', 'Cookie': token}
    payload = ''

    try:
        r = requests.put(endpoints.Booking + '/' + data.valid_id, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.BAD_REQUEST  # check the status code
