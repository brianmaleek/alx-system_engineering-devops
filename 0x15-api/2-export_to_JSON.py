#!/usr/bin/python3
"""
1. Extend th Python script to export data in the JSON format.
2. Requirements:
    a. Records all tasks that are owned by this employee
    b. Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
        TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    c. File name must be: USER_ID.json
"""

import json
import requests
from sys import argv

base_url = "http://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    user_data = get_user_data(employee_id)
    if not user_data:
        print(f"User with ID {employee_id} not found.")
        return

    username = user_data['username']
    task_data = get_task_data(employee_id)

    if not task_data:
        print(f"No task data found for user {username}.")
        return

    export_to_json(employee_id, username, task_data)


def get_user_data(employee_id):
    response = requests.get(f"{base_url}/users/{employee_id}")
    if response.status_code == 200:
        return response.json()
    return None


def get_task_data(employee_id):
    response = requests.get(f"{base_url}/todos",
                            params={"userId": employee_id})
    if response.status_code == 200:
        return response.json()
    return []


def export_to_json(employee_id, username, task_data):
    data_to_export = {
        str(employee_id):
        [
            {
                "task": task["title"], "completed": task["completed"],
                "username": username,
            }
            for task in task_data
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(data_to_export, jsonfile)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: 2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_data(employee_id)
