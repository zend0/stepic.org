#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Шаг 5

m = dict()

def avg(x):
	cnt = 0
	summ = 0

	for i in range(len(x)):
		summ += x[i]
		cnt += 1

	return(summ / cnt)

with open('/tmp/dataset_3380_5.txt') as inf:
	for line in inf:
		a,b,c = line.strip().split('\t')
		if int(a) in m:
			m[int(a)].append(int(c))
		else:
			m[int(a)] = [int(c)]

for i in range(1,12):
	if i in m:
		print(i, avg(m[i]))
	else:
		print(i, '-')

