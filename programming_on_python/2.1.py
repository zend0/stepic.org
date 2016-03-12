#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#n = int(input())

'''
c = 1
while c <= n:
	print('*' * c)
	c += 1
'''

'''
stars = '*'
while len(stars) < n :
	print(stars)
	stars += '*'
'''
'''
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
'''
'''
a = int(input())
s = 0
while a != 0:
	s += a
	a = int(input())
print(s)
'''

a = int(input())
b = int(input())

c = min(a,b)

while c%b != 0 or c%a != 0:
	c += 1

print(c)
