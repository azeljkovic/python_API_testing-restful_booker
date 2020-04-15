import requests
import endpoints
import data
from fixtures import get_token


def testDeleteBookingValidID(get_token):
    token = get_token
    headers = {'Cookie': token}

    try:
        r = requests.delete(endpoints.Booking + '/' + data.valid_id_2, headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.OK  # check the status code


def testDeleteBookingInvalidID(get_token):
    token = get_token
    headers = {'Cookie': token}

    try:
        r = requests.delete(endpoints.Booking + '/' + data.invalid_id, headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.NOT_FOUND  # check the status code


def testDeleteBookingUnauthorized():
    try:
        r = requests.delete(endpoints.Booking + '/' + data.valid_id)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.UNAUTHORIZED  # check the status code