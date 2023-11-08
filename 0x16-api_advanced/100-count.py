#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should
not).
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, instances=None, after=None, count=0):
    """
    Args:
    subreddit (str): The subreddit to search.
    word_list (list): The list of words to search for in post titles.
    instances (obj): Key/value pairs of words/counts.
    after (str): The parameter for the next page of the API results.
    count (int): The parameter of results matched thus far.
    """

    if instances is None:
        instances = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")

        for child in data.get("children"):
            title = child.get("data").get("title").lower().split()
            for word in word_list:
                word = word.lower()
                if word in title:
                    times = title.count(word)
                    instances[word] += times

        if after is None:
            if not instances:
                print("")
                return
            sorted_instances = sorted(instances.items(),
                                      key=lambda x: (-x[1], x[0]))
            for word, count in sorted_instances:
                print(f"{word}: {count}")
        else:
            count_words(subreddit, word_list, instances, after, count)
    else:
        print("Invalid subreddit.")
        return
