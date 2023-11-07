#!/usr/bin/python3
"""
function queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    return number of subscribers for a given subreddit
    return 0 if subreddit given is invalid
    """
    # Reddit API base url
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # get user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # send GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        for post in data.get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
