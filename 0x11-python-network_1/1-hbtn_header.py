#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""
import sys, urllib.request
with urllib.request.urlopen(urllib.request.Request(sys.argv[1])) as response:
    print(dict(response.headers).get("X-Request-Id"))


