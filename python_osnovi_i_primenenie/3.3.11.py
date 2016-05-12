#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.search(r"\b(\w+)\1\b", line)
    if res:
        print(line)
