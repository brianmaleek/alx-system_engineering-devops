#!/usr/bin/python3
"""
function queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    return number of subscribers for a given subreddit
    return 0 if subreddit given is invalid
    """
    # Reddit API base url
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # get user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # send GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        return data.get('subscribers')
    else:
        return 0
