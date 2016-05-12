#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.sub(r"human", "computer", line)
    print(res)
