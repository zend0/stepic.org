#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mysplit(mystr, spl=''):
    if spl == ':':
        k = mystr.split(spl)
        if len(k) > 1:
            if k[0].strip() in classes:
                classes[k[0].strip()].extend(mysplit(k[1]))
            else:
                classes.update({k[0].strip(): mysplit(k[1])})
        else:
            classes.update({k[0].strip(): []})
    else:
        return mystr.split()

def mycheck(mystr):
    a, b = mystr.split()
    # print(k)
    # print(classes)
    if b in classes:
        # print(k[0])
        # print(classes[k[1]])
        if a in classes[b] or a == b:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

def newcheck(a, b):
    if b in classes:
        print('** ' + b + ' in classes')
        for i in classes[b]:
            print(' ** ' + i + ' in ' + str(classes[b]))
            if a == i:
                return 'Yes'
            else:
                return newcheck(i, a)
        return 'No'

classes = dict()

"""
n = int(input())
for ni in range(n):
    dd = str(input())
"""
n = ['A', 'B : A', 'C : A', 'D : B C', 'C : E']
for ni in n:
    mysplit(ni, ':')

print(classes)
"""
q = int(input())
for qi in range(q):
    print(mycheck(str(input())))
"""
q = ['A B', 'B D', 'C D', 'D A', 'A A', 'A D']
for qi in q:
    #print(mycheck(qi))
    a, b = qi.split()
    print(newcheck(a, b))

