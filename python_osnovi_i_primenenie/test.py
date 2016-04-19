#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

a = 'Hello'
print(sys.getrefcount('Hello'))
b = a
print(sys.getrefcount('Hello'))
c = [a, b]
print(sys.getrefcount('Hello'))
a = 'Bye'
print(sys.getrefcount('Hello'))
print(b)
