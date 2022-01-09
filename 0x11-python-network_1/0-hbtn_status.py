#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode("utf-8")))
