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

    if (response.status_code == 200):
        validate_json_chema("discover.json", response)
    else:
        print(response.content)

def test_discoverRecent():
    # data for request
    url = server + "/API/0.9/users/me?discoverRecent"

    # getting response
    response = requests.get(url, headers=token)

    if (response.status_code == 200):
        validate_json_chema("discoverRecent.json", response)
    else:
        print(response.content)

def test_search():
    # data for request
    url = server + "/API/0.9/users/me"

    # getting response
    response = requests.get(url, headers=token, params={"search": "Madonna"})

    if (response.status_code == 200):
        validate_json_chema("search.json", response)
    else:
        print(response.content)

def test_me():
    # data for request
    url = server + "/API/0.9/users/me"

    # getting response
    response = requests.get(url, headers=token)

    if (response.status_code == 200):
        validate_json_chema("me.json", response)
    else:
        print(response.content)

def test_getAccount():
    # data for request
    url = server + "/API/0.9/users/me?getAccount"

    # getting response
    response = requests.get(url, headers=token)

    if (response.status_code == 200):
        validate_json_chema("getAccount.json", response)
    else:
        print(response.content)

def test_logout():
    # data for request
    url = server + "/API/0.9/users/me?logout"

    # getting response
    response = requests.get(url, headers=token)

    assert response.status_code == 200, "Logged out"

# change json schemes for all methods with required params
# http://json-schema.org/example1.html
# Can price be 0