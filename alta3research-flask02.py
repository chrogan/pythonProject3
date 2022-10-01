#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""


import requests
import json
from pprint import pprint


def main():
    URL = "http://127.0.0.1:2224/lotr"
    resp = requests.get(URL).json()
    pprint(resp)

    str = resp.read()
    decoded = json.loads(str)

    print("LORD OF THE RINGS BOOKS:")
    print(decoded["docs"][0]["name"])
    print(decoded["docs"][1]["name"])
    print(decoded["docs"][2]["name"])


if __name__ == "__main__":
    main()
