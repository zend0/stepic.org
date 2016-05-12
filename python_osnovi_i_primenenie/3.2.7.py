#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def search_str(search, string, cnt=0):
    res = string.find(search)
    if res != -1:
        cnt += 1
        return search_str(search, string[res + 1:], cnt)
    else:
        return cnt

s = str(input())
t = str(input())

print(search_str(t, s))
