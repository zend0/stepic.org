#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    res = re.sub(r"\b([\w]{1})([\w]{1})", r"\2\1", line)
    print(res)
