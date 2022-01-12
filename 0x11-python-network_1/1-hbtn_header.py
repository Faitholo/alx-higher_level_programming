#!/usr/bin/python3
"""A script that takes in a URL,
Sends a request to the URL,
And displays the value of the X-Request-Id variable found in the header ofthe response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
