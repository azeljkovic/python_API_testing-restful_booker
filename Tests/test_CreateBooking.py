import requests
import endpoints
import json
from pathlib import Path
import data


def testCreateBookingValid():
    headers = {'content-type': 'application/json'}
    file_request = Path('../JSON/request_create_valid.json')
    file_response = Path('../JSON/response_create_valid.json')
    with open(file_request) as f:
        payload = json.load(f)
    with open(file_response) as f:
        expected_response = json.load(f)

    try:
        r = requests.post(endpoints.Booking, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    assert r.status_code == data.OK  # check the status code
    assert response == expected_response  # check the response
