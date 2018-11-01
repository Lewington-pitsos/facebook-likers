# Generates a details dict

import random
import json
import os

name_files_female = [
    "female-de.json",  "female-fr.json", 
    "female-en.json",  "female-it.json", 
    "female-es.json",  "female-nl.json" 
]

name_files_male = [
    "male-de.json",  "male-fr.json",
    "male-en.json",  "male-it.json",
    "male-es.json",  "male-nl.json"
]

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Nov",
    "Oct",
    "Dec",
]

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()1234567890"

def random_name(male=True):
    # Change directory so we can find the name files
    original_directory = os.getcwd()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    name_files = name_files_male if male else name_files_female

    with open("./names/" + random.choice(name_files)) as name_file:
        names = json.load(name_file)
    
    # Return directory to what it was before
    os.chdir(original_directory)

    return (random.choice(names), random.choice(names))

def random_name_string():
    return " ".join(random_name(random.randint(0, 1) == 0))

def password():
    password = ""
    for _ in range(random.randint(10, 16)):
        password += random.choice(chars)
    
    return password

def new():
    male = random.randint(0, 1) == 0

    details = {
        "birth_day": random.randint(1, 28),
        "birth_month": random.choice(months),
        "birth_year": random.randint(1957, 1998),
        "male": male,
        "password": password()
    }
    details["first_name"], details["last_name"] = random_name(male)

    return details