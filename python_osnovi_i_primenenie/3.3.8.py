#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"\bcat\b", line)
    # print(res)
    if res:
        print(line)
