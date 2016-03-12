#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


def mysend(sock, msg):

    totalsent = 0

    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent += sent


req = 'Hello tcp!'
req_array = ['Hello tcp!', 'The world is my', 'close', 'New message']
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # создаём сокет
s.connect(('127.0.0.1', 2222))
# s.send(req.encode('utf8'))

for mess in req_array:
    s.send(mess.encode('utf8'))
    rsp = s.recv(1024)
    print(rsp)

s.close()