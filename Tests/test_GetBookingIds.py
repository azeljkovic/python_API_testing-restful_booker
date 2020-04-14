import requests
import endpoints
import data


def testGetAllIDs():
    try:
        r = requests.get(endpoints.Booking)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    ids = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(ids) == sorted(data.all_ids)  # check if all booking IDs are returned


def testGetIdsByFirstName():
    payload = {'firstname': data.valid_first_name}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingFirstName():
    payload = {'firstname': data.non_existing_first_name}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    expected_ids = []
    ids = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(ids) == sorted(expected_ids)  # check if response is empty


def testGetIdsByLastName():
    payload = {'lastname': data.valid_last_name}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    print(response)
    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingLastName():
    payload = {'lastname': data.non_existing_last_name}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    expected_ids = []
    ids = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(ids) == sorted(expected_ids)  # check if response is empty


def testGetIdsByCheckinDate():
    payload = {'checkin': data.valid_checkin_date}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingCheckinDate():
    payload = {'checkin': data.non_existing_date}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    expected_ids = []
    ids = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(ids) == sorted(expected_ids)  # check if response is empty


def testGetIdsByInvalidFormatCheckinDate():
    payload = {'checkin': data.invalid_format_date}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # response = r.json()

    assert r.status_code == requests.codes.ok  # check the status code
    #assert response == "Some valid error message"  # check if appropriate message ia provided


def testGetIdsByCheckoutDate():
    payload = {'checkout': data.valid_checkout_date}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingCheckoutDate():
    payload = {'checkout': data.non_existing_date}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    expected_ids = []
    ids = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(ids) == sorted(expected_ids)  # check if response is empty


def testGetIdsByInvalidFormatCheckoutDate():
    payload = {'checkout': data.invalid_format_date}
    try:
        r = requests.get(endpoints.Booking, params=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # response = r.json()

    assert r.status_code == requests.codes.ok  # check the status code
    # assert response == "Some valid error message"  # check if appropriate message ia provided


'''
helper functions
'''


def getIDsFromResponse(resp):
    id_array = []

    for key in resp:
        id_array.append(key.get("bookingid"))

    return id_array
