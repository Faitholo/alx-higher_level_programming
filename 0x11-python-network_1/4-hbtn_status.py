#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
