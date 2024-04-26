#!/usr/bin/python3
import urllib.request

"""This is a script which fetches a status for a particular url"""

def fetch_status():
    """Fetches the status of the provided URL and displays the response body."""

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    # Print type of body
    print(f"\t- type: {type(body)}")
    # Print encoded content (bytes)
    print(f"\t- content: {body}")
    # Decode and print content as UTF-8 string
    print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
  fetch_status()
