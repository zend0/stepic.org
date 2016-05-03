#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание не сделал, код не проходит тесты
"""

class ConvData:

    def __init__(self):
        self.cls = dict()
        self.parlst = list()

    def dspl(self, inp):
        if inp.find(':') != -1:
            try:
                k, v = inp.split(':')
            except ValueError:
                v = None
            else:
                v = (v.strip()).split()
            return {k.strip(): v}
        else:
            return {inp.strip(): None}

    def dadd(self, data):
        self.cls.update(self.dspl(data))

    def gparent(self, val):
        if self.cls[val] is not None:
            for p in self.cls[val]:
                self.gparent(p)
        else:
            self.parlst.append(val)

    def sparent(self, val):
        del self.parlst[:]
        self.gparent(val)
        # print('>>> ' + val + ' - ' + str(self.parlst))
        for i in range(len(self.parlst)):
            if val == self.parlst[i]:
                self.parlst.pop(i)

ml = list()
x = ConvData()

# n = range(int(input()))
# n = ['ArithmeticError', 'ZeroDivisionError : ArithmeticError', 'OSError', 'FileNotFoundError : OSError']
# n = ["10", "11 : 10", "12 : 11", "20", "13 : 11 20", "21 : 20"]
n = ['1 : 2 3 4', '2 : 5 3 6 7 8 9', '5 : 8', '3 : 4 9', '10 : 7', '4', '6 : 3 4', '7 : 6', '8 : 10 4 6 7', '9']
for i in n:
    x.dadd(i)
    # x.dadd(str(input()))

"""
m = range(int(input()))
for i in m:
    ml.append(str(input()))
"""
# ml = ['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']
# ml = ["20", "13", "10", "11", "21", "12"]
ml = ['6', '9', '4', '5', '10', '1', '3', '2', '8', '7']
for i in range(len(ml)):
    # print('in ' + str(ml[i]))
    x.sparent(ml[i])
    for pi in x.parlst:
        if pi in ml[0:i+1]:
            print(ml[i])

print(x.cls)
