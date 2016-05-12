#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.match(r"\b(a+)\b", "argh", line, count=1, flags=re.IGNORECASE)
    print(res)
