#!/usr/bin/env python
# -*- coding: utf-8 -*-


def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x

for i in range(15):
    print(str(i) + ' - ' + str(closest_mod_5(i)))

