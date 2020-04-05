import requests
import json
import endpoints
import pytest


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
    assert sorted(IDs) == sorted(expectedIDs)  # check if all booking IDs are returned


def testGetIdsByLastName():
    payload = {'lastname': 'Jackson'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()
    
    first_id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok #check the status code
    assert type(first_id) == int  # check if id exists in response


def testGetIdsByNonExistingLastName():
    payload = {'lastname': 'hfjhgjg'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()

    expectedIDs = []
    IDs = getIDsFromResponse(response)

    assert r.status_code == requests.codes.ok  # check the status code
    assert sorted(IDs) == sorted(expectedIDs)  # check if all booking IDs are returned


'''
helper functions below
'''


def getIDsFromResponse(resp):
    id_array = []

    for key in resp:
        id_array.append(key.get("bookingid"))
        
    return id_array