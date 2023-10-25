#!/usr/bin/python3

"""
1. Extend Python script to export data in the JSON format.
2. Requirements:
    a. Records all tasks from all employees
    b. Format must be: { "USER_ID": [ {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username":
    "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    c. File name must be: todo_all_employees.json
"""

import json
import requests
from sys import argv

base_url = "http://jsonplaceholder.typicode.com"


def get_all_employee_data():
    user_data = get_all_user_data()
    if not user_data:
        print("No user data found.")
        return

    all_data = {}
    for user in user_data:
        employee_id = user['id']
        username = user['username']
        task_data = get_task_data(employee_id)

        if not task_data:
            print(f"No task data found for user {username}.")
        else:
            all_data[employee_id] = [
                {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"],
                }
                for task in task_data
            ]

    export_to_json(all_data)


def get_all_user_data():
    response = requests.get(f"{base_url}/users")
    if response.status_code == 200:
        return response.json()
    return None


def get_task_data(employee_id):
    response = requests.get(f"{base_url}/todos",
                            params={"userId": employee_id})
    if response.status_code == 200:
        return response.json()
    return []


def export_to_json(data_to_export):
    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(data_to_export, jsonfile)


if __name__ == "__main__":
    if len(argv) != 1:
        print("Usage: 3-dictionary_of_list_of_dictionaries.py")
    else:
        get_all_employee_data()
