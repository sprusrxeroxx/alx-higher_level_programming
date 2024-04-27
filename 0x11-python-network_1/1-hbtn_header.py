#!/usr/bin/python3
import urllib.request
import sys

"""This a script Fetches the X-Request-Id header
    from the given URL.
"""

def get_request_id(url):


    try:
        with urllib.request.urlopen(url) as response:
            headers = response.headers
        request_id = headers.get("X-Request-Id")
        if request_id:
            print(request_id)
        else:
            print("X-Request-Id header not found.")
    except urllib.error.URLError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_request_id(sys.argv[1])
