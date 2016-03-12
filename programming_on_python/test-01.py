#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

a = float(input())
c = float(input())
b = str(input())

if b == '+' :
	print(a+c)
elif b == '-' :
        print(a-c)
elif b=='/' and c==0:
        print('Деление на 0!')
elif b=='/':
        print(a/c)
elif b=='*':
        print(a*c)
elif b=='mod':
        print(a%c)
elif b=='pow':
        print(a**c)
elif b=='div':
        print(a//c)

