#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, timedelta

endate = str(input())
endelta = int(input())
mydate = endate.split()

c_data = date(int(mydate[0]), int(mydate[1]), int(mydate[2])) + \
               timedelta(days=endelta)

print(str(c_data.year) + ' ' + str(c_data.month) + ' ' + str(c_data.day))
