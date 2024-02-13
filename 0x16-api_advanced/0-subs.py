#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subs
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None:
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        data = response.json()
        return data.get('data').get('subscribers')
    except Exception:
        return 0
