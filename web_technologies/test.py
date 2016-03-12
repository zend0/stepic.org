#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util


class MyTest:

    tap = 'Anton'

    def __init__(self, name, gender):

        self.name = name
        self.gender = gender
        self.var1 = 'Antonina'
        self.myprint('Hello World!')

    def myprint(self, mess=None):

        name = 'Irina'

        print(mess)
        print(name)

    def myprint02(self):

        print(self.tap)
        print(self.var1)

my_t_class = MyTest('Dmitry', 'male')
util.dtest(my_t_class)
my_t_class.myprint()
my_t_class.myprint02()

print(util.a)