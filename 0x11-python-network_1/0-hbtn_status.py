#!/usr/bin/python3
import urllib.request

"""This is a script which fetches a status for a particular url"""

def fetch_status():
  """Fetches the status of the provided URL and displays the response body."""
  url = "https://alx-intranet.hbtn.io/status"
  try:
    with urllib.request.urlopen(url) as response:
      data = response.read().decode('utf-8')
      # Print the response body with a tab before each line
      print("\t".join(data.splitlines()))
  except urllib.error.URLError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  fetch_status()
