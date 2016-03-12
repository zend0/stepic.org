#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
import requests

r = requests.get('http://ya.ru')
print(r.text)
'''

'''
# Шаг 2
import requests

cnt = 0

with open('/tmp/dataset_3378_2.txt') as inf:
	a = inf.readline().strip()

r = requests.get(a)
page = r.text

for i in page. splitlines():
	cnt += 1

print(cnt)
'''

# Шаг 3
import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
mystr = 'we'

with open('/tmp/dataset_3378_3.txt') as inf:
	a = inf.readline().strip()

r = requests.get(a)
page = r.text

while mystr not in page.lower():
	r = requests.get(url+page)
	page = r.text
	print(page)
