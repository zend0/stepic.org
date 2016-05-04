#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pg_class import sqlighter

# SQL
DB = {
    'host': '192.168.110.240',
    'name': 'tele',
    'user': 'tele',
    'pass': 'tele'
}

db_worker = sqlighter(DB)

print("* Проверка подключения к БД")
print(db_worker.cursor())

print("* SELECT")

print("* INSERT")
