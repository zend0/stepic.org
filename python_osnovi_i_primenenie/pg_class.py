#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2


class sqlighter:

    def __init__(self, DB):

        self.host = DB['host']
        self.db = DB['name']
        self.user = DB['user']
        self.passwd = DB['pass']
        self.con = None

    def cursor(self):

        try:
            self.con = psycopg2.connect(database=self.db, user=self.user, password=self.passwd, host=self.host)
            self.con.autocommit = True
        except psycopg2.OperationalError:
            print('server closed the connection unexpectedly')
        else:
            return self.con.cursor()

    def execute(self, query, data=()):

        cursor = self.cursor()
        # print(cursor.mogrify(query, data))
        cursor.execute(query, data)
        return cursor

    def select_all(self, query, data=()):

        """ Получаем все строки """
        cur = self.execute(query, data)
        row = cur.fetchall()
        cur.close()
        return row

    def select_single(self, query, data=()):

        """ Получаем одну строку """
        cur = self.execute(query, data)
        row = cur.fetchone()
        cur.close()
        return row

    def inup(self, query, data=()):

        """ выполнить INSERT или UPDATE """
        cur = self.execute(query, data)
        cur.close()

    def close(self):

        """ Закрываем текущее соединение с БД """
        self.con.close()