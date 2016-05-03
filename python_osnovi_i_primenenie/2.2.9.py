#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from simplecrypt import decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt") as inf:
    for line in inf:
        line = line.strip()
        try:
            dec = decrypt(line, encrypted)
        except:
            print('*** ' + line)
        else:
            print(dec)
