# python_API_testing-restful_booker

This is a sample project for automated API testing with Python Requests + PyTest for [Restful-booker] API.  
Toolchain used for this project is: 
- Python Requests: https://requests.readthedocs.io/en/master/
- PyTest: https://docs.pytest.org/en/latest/

## Installation
Python: https://www.python.org/downloads/  
Requests: https://requests.readthedocs.io/en/master/user/install/   
PyTest: https://docs.pytest.org/en/latest/getting-started.html

## How to run tests
Tests can be ran using one of the following commands:  

```pytest``` - run the whole test suite  
```pytest .\Tests\test_cart.py``` - run tests within the specified file  
```pytest .\Tests\test_cart.py -k 'testAddToCart'``` - run the specific test  


[Restful-booker]: <https://restful-booker.herokuapp.com/apidoc/index.html>
