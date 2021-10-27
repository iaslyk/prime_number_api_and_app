import requests


BASE = "http://127.0.0.1:5000/"


print("Enter integer: ")
input_number = int(input())


response = requests.get(BASE + "prime/" + str(input_number))
print(response.json())
