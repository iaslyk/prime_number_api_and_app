Restful Api for prime numbers created with Flask


This is a project that uses Flask made RESTful api to generate prime numbers between 2 and n, where n is user inputed integer.

Requirements:
    python_version: "3.9"
    pipenv
    Use pipenv to install dependencies from Pipfile with command pipenv install


To start project you need to run api.py with command "python api.py". This will start flask app server on "http://127.0.0.1:5000/".

You can use "http://127.0.0.1:5000/prime/n" to generate list of prime numbers, where n is user inputed number.

For example:
http://127.0.0.1:5000/prime/44 will return: ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43']


You can also use "python test.py" while running server to show inputed list in teminal.



This project is still developed and updated, and Readme file will also be updated when new features are added.
