#!/usr/bin/python3
"""script that REST API to get info about employee ID"""


import requests
import sys


def employee_todo_progress(employee_id):
    """
    Function that will get information about and employee's
    todo progress
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    empoyee_name = user_data['name']

    total_task = len(todo_data)
    completed_tasks = 0
    for todo in todos_data:
        if todo['completed']:
            completed_tasks += 1

    print(f'Employee {employee_name} is done with \
          tasks({completed_tasks}/{total_tasks}): ')
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee.id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
