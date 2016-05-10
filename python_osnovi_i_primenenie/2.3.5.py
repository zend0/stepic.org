#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def check_numb(num):
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def primes():
    n = 2
    while True:
        if check_numb(n):
            yield n
        n += 1

print(list(itertools.takewhile(lambda x: x <= 55, primes())))
