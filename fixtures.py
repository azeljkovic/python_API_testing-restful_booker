import requests
import json
import pytest
import endpoints
import data


@pytest.fixture(scope='session')
def get_token():
    payload = {"username": data.USERNAME, "password": data.PASSWORD}

    try:
        r = requests.post(endpoints.CreateToken, data=json.dumps(payload), headers=data.HEADERS)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    cookie = 'token=' + response['token']
    return cookie
