#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
# Шаг 1
a = [int(i) for i in input().split()]
m = a[0]

for x in a:
	if m > x:
		m = x

print(m)
'''
'''
# Шаг 4 (сапёр)
n, m, k = [int(i) for i in input().split()]
a = [[0 for j in range(m)] for i in range(n)]

for i in range(k):
	row, col = [int(i) - 1 for i in input().split()]
	a[row][col] = -1

for i in range(n):
	for j in range(m):
		if a[i][j] == 0:
			for di in range(-1,2):
				for dj in range(-1,2):
					ai = i + di
					aj = j + dj
					# (ai, aj)
					if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
						a[i][j] += 1

for i in range(n):
	for j in range(m):
		if a[i][j] == -1:
			print('*', end='')
		elif a[i][j] == 0:
			print('.', end='')
		else:
			print(a[i][j], end='')
	print()
'''

'''
# Шаг 7
s = -1
arr = []

while s != 0:
	a = int(input())
	arr.append(a)
	
	s = 0
	for i in arr:
		s += i

s = 0
for i in arr:
	s += i * i

print(s)
'''
'''
# Шаг 8
n = int(input())
b = []

for i in range(n):
	a = [i for j in range(i)]
	b = b + a

for j in b[:n]:
	print(j, end=' ')
'''
'''
# Шаг 9
lst = [int(i) for i in input().split()]
x = int(input())
pos = []

for i in range(len(lst)):
	if lst[i] == x:
		pos.append(i)

if len(pos) == 0:
	print('Отсутствует')
else:
	for j in pos:
		print(j, end=' ')
'''

# Шаг 10
st = input()
crt = []
gen = []

# получаем вводные данные
while st != "end":
    crt.append([int(i) for i in st.split()])
    st = input()

# генерируем новую нулевую матрицу
for i in range(len(crt)):
	gen.append([0 for j in range(len(crt[i]))])

for i in range(len(gen)):
	for j in range(len(gen[i])):
		if i == 0 and i != len(gen)-1:
			im = len(gen)-1
		else:
			im = i - 1
		
		if i != 0 and i == len(gen)-1:
			ip = 0
		else:
			ip = i + 1
		
		if j == 0 and j != len(gen[i])-1:
			jm = len(gen[i])-1
		else:
			jm = j - 1
		
		if j != 0 and j == len(gen[i])-1:
			jp = 0
		else:
			jp = j + 1
		
		gen[i][j] = crt[im][j] + crt[ip][j] + crt[i][jm] + crt[i][jp]

print(gen)
