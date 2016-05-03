#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def __init__(self):
        self.mylist = list()

    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError(x)

lst = PositiveList()

lst.append(2)
lst.append(3)
lst.append(-4)

print(lst)