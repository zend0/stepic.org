#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 'aaaa'

def dtest(inp_obj):

    print('BEGIN function')
    inp_obj.myprint()
    print(__file__)
    print('END function')


try:
    from local_util import *
except ImportError:
    pass