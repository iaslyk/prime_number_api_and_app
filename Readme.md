# Restful Api for prime numbers created with Flask


This is a project that uses Flask made RESTful api to generate first N prime numbers, and using Jinja template to render results on a web page.

## Requirements
**python_version: "3.9"**

**pipenv**

Use pipenv to install dependencies from Pipfile with command **pipenv install**



## How To Start
To start project you need to run api.py with command *python api.py*. This will start flask app server on "http://127.0.0.1:5000/".

When you start Flask server, you will need to enter (in terminal) how often (in seconds) will cache auto-clean itself.

You can use "http://127.0.0.1:5000/prime/n" to generate list of prime numbers, where n is user input number.

You can use "http://127.0.0.1:5000/prime/clear" to force clear all cache.

For example:
http://127.0.0.1:5000/prime/44 will return: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193]