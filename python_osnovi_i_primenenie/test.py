#!/usr/bin/env python3
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

print('-----------')

def h():
    print("- H")
    print("- 12")
    print("H - end")


def f():
    print("- F")
    g(h)
    print("F - end")


def g(a):
    print("- G - ", a)
    a()
    print("G - end")

print("\nMODULE")
g(f)

print('--------')

def s(a, *vs, b=10):
    res = a + b
    print(b)
    for v in vs:
        res += v
    return res

print('--------')
x = {'foo': {'parent': 'global', 'vars': ['b']},
      'global': {'parent': None, 'vars': ['a']},
      'bar': {'parent': 'foo', 'vars': ['a']}}

if 'a' in x['global']['vars']:
    print('!')
else:
    print(':(')