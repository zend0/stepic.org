#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mysplit(mystr, spl=''):
    if spl == ':':
        k = mystr.split(spl)
        if len(k) > 1:
            return {k[0]: mysplit(k[1])}
        else:
            return {k[0]}
    else:
        return mystr.split()


def mycheck(mystr):
    k = mystr.split()
    if k[1] in classes:
        if k[0] in classes[k[1]]:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

classes = dict()

n = int(input())

for ni in range(n):
    dd = str(input())
    classes.update(mysplit(dd, ':'))

q = int(input())
for qi in range(q):
    print(mycheck(str(input())))
