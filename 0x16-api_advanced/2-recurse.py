#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=None, after=None, count=0):
    """
    Recursive function that queries the Reddit API returns list of subreddit
    containing titles of all hot articles.
    Return: None if subreddit given is invalid.
    """
    if hot_list is None:
        hot_list = []

    # Reddit API base URL
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set a custom User-Agent to avoid getting blocked
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {"after": after, "count": count, "limit": 100}

    # Send a GET request to Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")

        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
    else:
        return None
