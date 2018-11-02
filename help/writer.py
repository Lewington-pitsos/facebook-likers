import json

def save_details(details):
    name = details["first_name"] + " " + details["last_name"]
    with open(name + ".json") as f:
        json.dump(details, f)