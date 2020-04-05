import requests
import endpoints


def testGetAllIDs():
    r = requests.get(endpoints.Booking)
    response = r.json()

    expectedIDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    IDs = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(IDs) == sorted(expectedIDs)  # check if all booking IDs are returned


def testGetIdsByFirstName():
    payload = {'firstname': 'Susan'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingFirstName():
    payload = {'firstname': 'vcxvcx'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    expectedIDs = []
    IDs = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(IDs) == sorted(expectedIDs)  # check if response is empty


def testGetIdsByLastName():
    payload = {'lastname': 'Jackson'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingLastName():
    payload = {'lastname': 'hfjhgjg'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    expectedIDs = []
    IDs = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(IDs) == sorted(expectedIDs)  # check if response is empty


def testGetIdsByCheckinDate():
    payload = {'checkin': '2016-09-21'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingCheckinDate():
    payload = {'checkin': '2222-09-21'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    expectedIDs = []
    IDs = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(IDs) == sorted(expectedIDs)  # check if response is empty


def testGetIdsByInvalidFormatCheckinDate():
    payload = {'checkin': '27.3.1943.'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    assert r.status_code == requests.codes.ok  # check the status code
    assert response == "Some valid error message"  # check if appropriate message ia provided


def testGetIdsByCheckoutDate():
    payload = {'checkout': '2020-03-23'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok  # check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingCheckoutDate():
    payload = {'checkout': '2222-09-21'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    expectedIDs = []
    IDs = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(IDs) == sorted(expectedIDs)  # check if response is empty

def testGetIdsByInvalidFormatCheckoutDate():
    payload = {'checkout': '27.3.1943.'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    assert r.status_code == requests.codes.ok  # check the status code
    assert response == "Some valid error message"  # check if appropriate message ia provided


'''
helper functions below
'''


def getIDsFromResponse(resp):
    id_array = []

    for key in resp:
        id_array.append(key.get("bookingid"))

    return id_array
