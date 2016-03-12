#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
# Шаг 2
b = ''
letters = []

with open('/home/sema/old.txt') as inf:
    a = inf.readline().strip()

for i in range(len(a)):
	if a[i].isalpha():
		letters.append(i)

#print(letters)		# 0, 1, 2 = [0, 2, 4]

for idlet in range(len(letters)):
	if letters[idlet] == max(letters):
		b = b + ( a[letters[idlet]] * int( a[ letters[idlet]+1 : len(a) ]) )
	else:
		b = b + ( a[letters[idlet]] * int( a[ letters[idlet]+1 : letters[idlet+1] ] ) )
print(b)

with open('/home/sema/new.txt', 'w') as ouf:
    ouf.write(b)
'''

'''
# Шаг 3
a = dict()
mk = ''
mv = 0

def counting(s):
	for i in s.split():
		if i in a:
			a[i] += 1
		else:
			a[i] = 1

with open('/tmp/text.txt') as inf:
	for line in inf:
		counting( line.lower().strip() )

#print(a)

for k, v in a.items():
	if v >= mv:
		tmpv = v
		tmpk = k
		# print(k,v,'--',mk,mv)
		if k > mk and v >= mv:
			mk = k
			mv = v
		else:
			mk = tmpk
			mv = tmpv

print(mk, mv)
'''

'''
# Шаг 4
m = dict()
cnt = 0

mat = []
fiz = []
rus = []

def avg(x):
	cnt = 0
	summ = 0

	for i in range(len(x)):
		summ += x[i]
		cnt += 1

	return(summ / cnt)

with open('/tmp/text.txt') as inf:
	for line in inf:
		a,b,c,d = line.strip().split(';')
		#print(line.strip().split(';'))
		m[cnt] = [int(b),int(c),int(d)]
		
		mat.append(int(b))
		fiz.append(int(c))
		rus.append(int(d))
		
		cnt += 1
		
with open('/tmp/new_file.txt', 'w') as ouf:
	for val in m.values():
		ouf.write(str(avg(val))+'\n')
	ouf.write(str(avg(mat))+' '+str(avg(fiz))+' '+str(avg(rus))+'\n')
'''
