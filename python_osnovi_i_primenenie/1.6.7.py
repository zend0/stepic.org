#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mysplit(mystr, spl=''):
    if spl == ':':
        k = mystr.split(spl)
        if len(k) > 1:
            return {k[0].strip(): mysplit(k[1])}
        else:
            return {k[0].strip(): []}
    else:
        return mystr.split()


def mycheck(mystr):
    k = mystr.split()
    # print(k)
    # print(classes)
    if k[1] in classes:
        # print(k[0])
        # print(classes[k[1]])
        if k[0] in classes[k[1]]:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

classes = dict()

"""
n = int(input())
for ni in range(n):
    dd = str(input())
"""
n = ['A', 'B : A', 'C : A', 'D : B C']
for ni in n:
    dd = ni
    classes.update(mysplit(dd, ':'))

"""
q = int(input())
for qi in range(q):
    print(mycheck(str(input())))
"""
q = ['A B', 'B D', 'C D', 'D A']
for qi in q:
    print(mycheck(qi))
