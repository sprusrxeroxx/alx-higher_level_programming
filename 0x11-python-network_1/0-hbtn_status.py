#!/usr/bin/python3
import urllib.request

"""This is a script which fetches a status for a particular url"""

def fetch_status():
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))

if __name__ == "__main__":
  fetch_status()
