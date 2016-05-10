#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("/tmp/dataset_24465_4.txt") as f:
    myf = f.read()
    myf = myf.splitlines()
    myf.reverse()

print('\n'.join(myf))
