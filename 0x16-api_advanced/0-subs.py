#!/usr/bin/python3
""" Script that counts the number of subscribers on reddit """
import requests


def number_of_subscribers(subreddit):
    """
    this function retuns the number of subscribers for reddit
    it does not redirect if endpoint is not found
    """

    url = f'https://www.reddit.com/r{subreddit}/about.json'
    headers = {'User-Agent': 'Myss/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except Exception as e:
        print(f'An error occured: {e}')
