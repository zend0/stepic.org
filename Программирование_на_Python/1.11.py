#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- 1 --
'''
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2

print( (p*(p-a)*(p-b)*(p-c)) ** 0.5 )
'''

# -- 2 --
'''
a = int(input())
if -15 < a <= 12 or 14 < a < 17 or a >= 19:
	print('True')
else:
	print('False')
'''

# -- 3 --
'''
a = float(input())
b = float(input())
c = str(input())

if c == '+':
	print(a + b)
elif c == '-':
	print(a - b)
elif c == '/':
	if b == 0:
		print("Деление на 0!")
	else:
		print(a / b)
elif c == '*':
	print(a * b)
elif c == 'mod':
	if b == 0:
		print("Деление на 0!")
	else:
		print(a % b)
elif c == 'pow':
	print(a ** b)
elif c == 'div':
	if b == 0:
		print("Деление на 0!")
	else:
		print(a // b)
'''

# -- 4 --
'''
t = str(input())

if t == 'треугольник':
	a = float(input())
	b = float(input())
	c = float(input())
	
	p = (a + b + c) / 2
	print( (p * (p-a) * (p-b) * (p-c)) ** 0.5)
elif t == 'прямоугольник':
	a = float(input())
	b = float(input())
	
	print(a * b)
elif t == 'круг':
	a = float(input())
	
	print(3.14 * a**2)
'''

# -- 5 --
'''
a = int(input())
b = int(input())
c = int(input())

mx = max(a,b,c)
mn = min(a,b,c)
ot = (a + b + c) - (mx + mn)

print(mx,'\n',mn,'\n',ot)
'''

# -- 6 --

# Для выявления остатка использовать %
# http://a-panov.ru/2010/05/%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5-%D0%BE%D0%BA%D0%BE%D0%BD%D1%87%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0-%D0%B8%D0%BB%D0%B8-%D1%87%D0%B8%D1%81%D0%BB%D0%B0/

n = int(input())

if n >= 100:
	nn = n % 100
else:
	nn = n

if nn % 10 == 1 and nn != 11:
	print(n,'программист') 
elif 1 < nn % 10 < 5 and not 11 < nn < 15:
	print(n,'программистa')
else:
	print(n,'программистов')
	

