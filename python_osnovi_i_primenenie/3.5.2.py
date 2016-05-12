#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

types = dict()

with open("/tmp/Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        dd = row[2].split()
        if dd[0] != 'Date':
            year = dd[0].split("/")
            if year[2] == '2015':
                if row[5] in types:
                    types[row[5]] += 1
                else:
                    types[row[5]] = 1

print(types)

