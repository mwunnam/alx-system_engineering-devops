#!/usr/bin/python3
""" Script that get all the top title posts"""
import requests


def recurse(subreddit, hot_list=None, after='', count=0):
    """
    This get all number of all the titles for the hot section
    """

    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Myss/0.1'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get('data')
    after = results.get('after')

    for result in results.get('children'):
        hot_list.append(result.get('data').get('title'))

    count += result.get('dist', 0)

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
