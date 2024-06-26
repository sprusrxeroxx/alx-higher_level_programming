import urllib.request
import urllib.parse
import sys

"""A script which sends a POST request 
    to the URL with the email as a parameter 
    and displays the response.
"""


def send_post_request(url, email):
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    request = urllib.request.Request(url, data)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode("utf-8")
        print(body)
    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len (sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)
    else:
       raise SyntaxError
