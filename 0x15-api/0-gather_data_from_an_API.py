#!/usr/bin/python3
"""
1. Python script uses REST API, for a given employee ID,
    returns information about his/her TODO list progress.
2. Use urllib or requests module
3. Script accepts an integer as a parameter, which is the employee ID
4. Script displays on the standard output the employee TODO list progress
    in this exact format:
        a. First line: Employee EMPLOYEE_NAME is done with tasks
            (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
                - EMPLOYEE_NAME: name of the employee
                - NUMBER_OF_DONE_TASKS: number of completed tasks
                - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is
                    the sum of completed and non-completed tasks
        b. Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "http://jsonplaceholder.typicode.com"

    # Get user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Failed to fetch user information.")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get TODOs for the user
    todos_response = requests.get(f"{base_url}/todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list information.")
        return

    todos_data = todos_response.json()
    completed_tasks = [task['title']
                       for task in todos_data if task.get('completed')]
    total_tasks = len(todos_data)

    print(
        f"Employee {employee_name} is done with tasks "
        f"({len(completed_tasks)}/{total_tasks}):"
        )

    for task in completed_tasks:
        print(f"    {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
