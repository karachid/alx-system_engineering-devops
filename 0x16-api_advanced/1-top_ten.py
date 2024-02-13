#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """It prints  the first 10 hot posts listed"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        datas = response.json().get('data').get('children')
        for data in datas:
            print(data.get('data').get('title'))
    except Exception:
        print("None")
