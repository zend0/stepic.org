#!/usr/bin/env python3
# -*- coding: utf-8 -*-

objects = [1, 2, 1, 2, 3, 4, 3, 3, 5]
print(len(set(objects)))

ans = 0
for ind in range(len(objects)):
    cnt = 0
    for ind2 in range(ind+1, len(objects)):
        if objects[ind] is objects[ind2]:
            cnt += 1
            break
    if cnt == 0:
        ans += 1
print(ans)
