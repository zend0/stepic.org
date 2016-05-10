#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path

my_path = "/tmp/"
list_dirs = list()

for current_dir, dirs, files in os.walk(my_path + 'main'):
    if list(filter(lambda x: x.endswith('.py'), files)):
        list_dirs.append(current_dir[len(my_path):])
    """
    # или
    if len(files) > 0:
        for file in files:
            if file.endswith(".py"):
                list_dirs.append(current_dir[len(my_path):])
                break
    """

list_dirs.sort()

with open('/tmp/result.txt', 'w') as res:
    res.write('\n'.join(list_dirs))
