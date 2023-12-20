#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    data = requests.get(f"{URL}users/{argv[1]}")
    data = data.json()
    user_name = data['username']

    data = requests.get(f"{URL}todos")
    all_todos = data.json()
    user_todos = [todo for todo in all_todos if todo['userId'] == int(argv[1])]

    user_dict = []

    for todo in user_todos:
        user_dict.append({"task": todo['title'],
                          "completed": todo['completed'],
                          "username": user_name})

    json_obj = {f"{user_id}": user_dict}

    with open(f"{user_id}.json", 'w') as f:
        json.dump(json_obj, f)
