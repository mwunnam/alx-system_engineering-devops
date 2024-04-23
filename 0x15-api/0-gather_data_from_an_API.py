#!/usr/bin/python3
"""script that REST API to get info about employee ID"""


import requests
import sys


def employee_todo_progress(employee_id):
    """
    Function that will get information about and employee's
    todo progress
    """
    """Setting up urls"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    """Getting user data"""
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    """Getting todo data"""
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)

    """Calculating task completed"""
    completed_tasks = 0
    for todo in todos_data:
        if todo['completed']:
            completed_tasks += 1

    progress_message = (
            f'Employee {employee_name} is done with tasks '
            f'({completed_tasks}/{total_tasks}): '
    )
    print(progress_message)
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee.id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
