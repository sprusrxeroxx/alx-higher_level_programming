#!/usr/bin/python3
import urllib.request

"""This is a script which fetches a status for a particular url"""

def fetch_status():
    """Fetches the status of the provided URL and displays the response body."""

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
  fetch_status()
