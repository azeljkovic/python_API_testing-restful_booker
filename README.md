# python_API_testing-restful_booker

This is a sample project for automated API testing with Python Requests + PyTest for [Restful-booker] API.  
Tools used for this project are: 
- Python Requests: https://requests.readthedocs.io/en/master/
- PyTest: https://docs.pytest.org/en/latest/

## Installation
Python: https://www.python.org/downloads/  
Requests: https://requests.readthedocs.io/en/master/user/install/   
PyTest: https://docs.pytest.org/en/latest/getting-started.html  

...or simply run it as a docker container.

## Configuration
I highly recommend running a local instance of the Restufl-booker as a software under test (see [github manual]), in order to avoid interference with other users.
This can be configure in ```endpoints.py``` file by uncommenting local or global URL.

## How to run tests (local environment)
Tests can be ran using one of the following commands:  

```pytest``` - run the whole test suite  
```pytest ./Tests/test_GetBooking.py``` - run tests within the specified file  
```pytest ./Tests/test_GetBooking.py -k 'testGetValidBooking'``` - run the specific test  

## How to run tests (docker)
```docker-compose build```  
```docker-compose up```

By default, this will run the whole test suite. If you want to change this behavior, feel free to modify docker-compose.yml or to run the container through the command line with appropriate command.


[Restful-booker]: <https://restful-booker.herokuapp.com/apidoc/index.html>
[github manual]: <https://github.com/mwinteringham/restful-booker>