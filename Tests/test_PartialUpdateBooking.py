import requests
import endpoints
import json
from pathlib import Path
import data
from fixtures import get_token


def testPartialUpdateBookingValid(get_token):
    token = get_token
    headers = {'content-type': 'application/json', 'Cookie': token}
    file_request = Path('../JSON/request_partial_update_valid.json')
    with open(file_request) as f:
        payload = json.load(f)

    try:
        r = requests.patch(endpoints.Booking + '/' + data.valid_id, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.OK  # check the status code


def testUpdateBookingInvalidID(get_token):
    token = get_token
    headers = {'content-type': 'application/json', 'Cookie': token}
    file_request = Path('../JSON/request_partial_update_valid.json')
    with open(file_request) as f:
        payload = json.load(f)

    try:
        r = requests.patch(endpoints.Booking + '/' + data.invalid_id, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.NOT_FOUND  # check the status code


def testPartialUpdateBookingEmptyRequest(get_token):
    token = get_token
    headers = {'content-type': 'application/json', 'Cookie': token}
    payload = ''

    try:
        r = requests.patch(endpoints.Booking + '/' + data.valid_id, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.BAD_REQUEST  # check the status code
