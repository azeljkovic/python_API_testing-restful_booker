import requests
import endpoints


def testGetValidBooking():
    r = requests.get(endpoints.Booking + '/1')
    response = r.json()

    print(response)


testGetValidBooking()