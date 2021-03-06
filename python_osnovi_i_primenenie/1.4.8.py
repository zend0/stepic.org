#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def createc(namespace, parent):
    if namespace not in x:
        x.update({namespace: {'parent': parent, 'vars': []}})


def addc(namespace, var):
    if namespace in x:
        x[namespace]['vars'].append(var)


def getc(namespace, var):
    if namespace in x:
        if var in x[namespace]['vars']:
            return namespace
        else:
            return getc(x[namespace]['parent'], var)
    else:
        return None


x = {'global': {'parent': None, 'vars': []}}
n = int(input())

if 1 <= n <= 100:
    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'create':
            createc(cmd[1], cmd[2])
        elif cmd[0] == 'add':
            addc(cmd[1], cmd[2])
        elif cmd[0] == 'get':
            print(getc(cmd[1], cmd[2]))

# print(x)
