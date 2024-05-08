#!/usr/bin/python3
""" Script return the top 10"""


import requests


def top_ten(subreddit):
    """
    Function get the top 10 post from reddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Myss'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print('None')
        return
