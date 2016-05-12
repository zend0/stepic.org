#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
НЕ сделал
"""


import re
import sys
import requests


def reqsts(link):
    res = requests.get(link)
    if res.status_code == 200:
        return res.text
    else:
        return False

links = list()

for line in sys.stdin:
    links.append(line.strip())

for link in links:
    # req_link = re.findall(r"href=\"(.*)\"", reqsts(link))
    req_link = re.match(r"href=\"([\w\s:/\.]+?)\"", 'href="aaa" href="bbb"')
    print(req_link.groups())
    """
    res = requests.get(line)
    if res.status_code == 200:
        link = re.search(r"href=\"(.*)\"", res.text)
        print(link.group(1))
    """

