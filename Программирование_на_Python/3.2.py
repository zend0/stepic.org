#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# Шаг 5
def update_dictionary(d, key, value):
	if key in d:
		d[key].append(value)
	else:
		if 2*key in d:
			d[2*key].append(value)
		else:
			d[2*key] = [value]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''

'''
# Шаг 6
a = dict()

for i in input().lower().split():
	if i in a:
		a[i] += 1
	else:
		a[i] = 1

for key, value in a.items():
	print(key, value)
'''

# Шаг 7
def f(x):
	x = x*2
	print(x , 'func')
	return(x)

a = dict()
n = int(input())

for i in range(n):
	x = int(input())
	if x in a:
		print(a[x])
	else:
		a[x] = f(x)
		print(a[x])
