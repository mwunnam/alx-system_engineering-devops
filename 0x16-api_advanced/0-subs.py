#!/usr/bin/python3
""" Script that counts the number of subscribers on reddit """
import requests


def number_of_subscribers(subreddit):
    """
    this function retuns the number of subscribers for reddit
    it does not redirect if endpoint is not found
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Myss/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0


if __name__ == "__main__":
    pass
