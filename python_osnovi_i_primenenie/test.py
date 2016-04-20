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

print('-----------')


def testt(*fi):
    print(fi)

lst = ['aa', 'bb']
testt('a', 'b', 'c', 'd')
