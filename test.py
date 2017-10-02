import pytest
import requests
import json

from jsonschema import validate

server = "https://conuremusic.com"
global token
token = {"Authorization": "Bearer 4b2bac7366a7781887e8cf1e8a0a8dd057ea89f1"}

def validate_json_chema(file, r):
    # open and load json scheme file
    schema_file = open(file, "r")
    schema_json = json.load(schema_file)

    # validation
    validate(r.json(), schema_json)

    # close json scheme file
    schema_file.close()

def test_discover():
    # data for request
    url = server + "/API/0.9/users/me?discover"

    # getting response
    response = requests.get(url, headers=token)
    # print(response.content)

    validate_json_chema("discover.json", response)

def test_discoverRecent():
    # data for request
    url = server + "/API/0.9/users/me?discoverRecent"

    # getting response
    response = requests.get(url, headers=token)

    validate_json_chema("discoverRecent.json", response)

def test_search():
    # data for request
    url = server + "/API/0.9/users/me?discover"

    # getting response
    response = requests.get(url, headers=token, params={"search": "Каста"})
    print(response.content)

    validate_json_chema("search.json", response)

test_discover()
test_discoverRecent()
test_search()

# change json schemes for all methods with required params
# http://json-schema.org/example1.html
# Can price be 0