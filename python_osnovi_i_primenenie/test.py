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
class Counter:
    pass

Counter.count = 1000

x = Counter
print(x.count)

z = Counter()
print(z.count)
#z.count = 2

x.count = 100

print(x.count)
print(z.count)

x1 = Counter
x1.count = 200
print(x1.count)
print(x.count)

