#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# Шаг 9
sum = 0

for key in [int(i) for i in input().split()]:
	sum += key

print(sum)
'''

'''
# Шаг 10
a = [int(i) for i in input().split()]

if len(a) != 1:
	for key in range(len(a)):
		sum = 0
		if key == 0:
			sum = a[-1] + a[key+1]
		elif key == len(a)-1:
			sum = a[key-1] + a[0]
		else:
			sum = a[key-1] + a[key+1]
		print(sum, end=' ')
else:
	print(a[0], end=' ')
'''

# Шаг 11
a = [int(i) for i in input().split()]
a.sort()
cnt = 1

for key in range(len(a)):
	if a[key] == a[key-1] and key != 0:
		cnt += 1
	else:
		cnt = 1
	
	if cnt == 2:
		print(a[key], end=' ')
