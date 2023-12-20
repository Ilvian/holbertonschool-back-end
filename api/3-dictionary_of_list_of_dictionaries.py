#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format
"""


import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    data = requests.get(f"{URL}users")
    user_data = data.json()

    data = requests.get(f"{URL}todos")
    all_todos = data.json()

    user_json = {}
    for user in user_data:
        user_todos = []
        for todos in all_todos:
            if todos['userId'] == user['id']:
                user_todos.append({"username": user['username'],
                                   "task": todos['title'],
                                   "completed": todos['completed']})
        user_json[f"{user['id']}"] = user_todos

    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_json, f)
