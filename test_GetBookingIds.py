import requests
import json
import endpoints
import pytest


def testGetAllIDs():
    r = requests.get(endpoints.Booking)
    response = r.json()
    id = response[0].get("bookingid")

    assert r.status_code == requests.codes.ok #check the status code
    assert type(id) == int                    #check that at least one bookingid exist

def testGetIdsByFirstName():
    payload = {'firstname': 'Mary'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()
    print(response)

    assert r.status_code == requests.codes.ok #check the status code

def testGetIdsByLastName():
    payload = {'lastname': 'Brown'}
    r = requests.get(endpoints.Booking, params=payload)
    response = r.json()
    print(response)

    assert r.status_code == requests.codes.ok #check the status code



testGetIdsByFirstName()

