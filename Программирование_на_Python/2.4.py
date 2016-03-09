#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
s = input()
cnt = 0

for i in s.upper():
	if i == 'C' or i == 'G':
		cnt += 1

print(cnt/len(s)*100)
'''
'''
s = "abcdefghijk"
new = ''

new = new + s[3:6] + ' '
new = new + s[:6] + ' '
new = new + s[3:] + ' '
new = new + s[::-1] + ' '
new = new + s[-3:] + ' '
new = new + s[:-6] + ' '
new = new + s[-1:-10:-2]

print(new)
'''

s = 'abc'
crypt = ''

pos = 0
lst = ''
cnt = 1

for i in s:
	if i != lst and lst != '':
		crypt = crypt + lst + str(cnt)

	if i == lst:
		cnt += 1
	else:
		lst = i
		cnt = 1
	
	# print(i, cnt)
	pos += 1

crypt = crypt + lst + str(cnt)
print(crypt)
