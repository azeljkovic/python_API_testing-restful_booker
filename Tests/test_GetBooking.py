import requests
import endpoints
import data


def testGetValidBooking():
    try:
        r = requests.get(endpoints.Booking + '/' + data.valid_id)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()

    firstname = response.get("firstname")
    lastname = response.get("lastname")
    totalprice = response.get("totalprice")
    depositpaid = response.get("depositpaid")
    bookingdates = response.get("bookingdates")
    checkin = bookingdates.get("checkin")
    checkout = bookingdates.get("checkout")

    assert r.status_code == data.OK  # check the status code
    assert type(firstname) == str  # check if first name exists in response
    assert type(lastname) == str  # check if last name exists in response
    assert type(totalprice) == int  # check if total price exists in response
    assert type(depositpaid) == bool  # check if deposit paid exists in response
    assert type(checkin) == str  # check if checkin exists in response
    assert type(checkout) == str  # check if checkout exists in response


def testGetInvalidBooking():
    try:
        r = requests.get(endpoints.Booking + '/' + data.invalid_id)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    assert r.status_code == data.NOT_FOUND  # check the status code
    assert r.text == "Not Found"
