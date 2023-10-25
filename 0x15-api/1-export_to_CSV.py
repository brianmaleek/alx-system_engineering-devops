#!/usr/bin/python3
"""
1. Using what you did in the task #0, extend the Python script to export data
    in the CSV format.
2. Requirements:
        a. Record all tasks that are owned by this employee
        b. Format must be: "USER_ID","USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        c. File name must be: USER_ID.csv
"""
import csv
import requests
import sys

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

    export_to_csv(employee_id, username, task_data)


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


def export_to_csv(employee_id, username, task_data):
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for task in task_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": task["completed"],
                "TASK_TITLE": task["title"]
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_data(employee_id)
