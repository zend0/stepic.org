#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
# Шаг 2
def f(n):
	return n * 10 + 5

print(f(f(f(10))))
'''

'''
# Шаг 5
def append_zero(xs):
	xs.append(2)
	xs.append(3)

a=[2]
append_zero(a)
print(a)
'''

'''
# Шаг 7
def f(x):
	if x <= -2:
		return(1-(x+2)**2)
	if -2 < x <= 2:
		return(-x/2)
	if x > 2:
		return((x-2)**2 + 1)

print(f(1))
'''

'''
# Шаг 8
def modify_list(l):
	for i in range(len(l)-1, -1, -1):
		if l[i] % 2 != 0:
			del l[i]
		else:
			l[i] = l[i] // 2

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
'''

