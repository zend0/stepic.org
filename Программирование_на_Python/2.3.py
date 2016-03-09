#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''
a = int(input())	# вертикаль
b = int(input())	# вертикаль
c = int(input())
d = int(input())

print('\t', end='')
for z in range(c,d+1):
	print(z, end='\t')
print()

for i in range(a,b+1):
	print(i, end='\t')
	for j in range(c,d+1):
		print(i*j, end='\t')
	print()
'''

# Шаг 7
a = int(input())
b = int(input())
s = 0
count = 0

for j in range(a, b+1):
	if j % 3 == 0:
		s += j
		count += 1

print(s / count)

