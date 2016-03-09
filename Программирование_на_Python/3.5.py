#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
import sys
print(len(sys.argv))
'''
'''
import subprocess

subprocess.call(["python3","-h"])
#subprocess.call(["uname"])
#subprocess.call(["ls", "-l"])
'''

'''
# Шаг 2
import math
r = float(input())
print(2*math.pi*r)
'''

# Шаг 3
import sys

for i in range(len(sys.argv)):
	if i != 0:
		print(sys.argv[i], end=' ')

