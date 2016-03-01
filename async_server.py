#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncore
import socket


class EchoHandler(asyncore.dispatcher_with_send):


    def handle_read(self):
        data = self.recv(1024)
        if data:
            if data == 'close':
                self.close()
            self.send(data)
        else:
            self.close()


class EchoServer(asyncore.dispatcher):


    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(10)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            # print('Incoming connection from %s' % repr(addr))
            handler = EchoHandler(sock)


server = EchoServer('0.0.0.0', 2222)
asyncore.loop()

"""
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if data == 'close':
            break
        conn.send(data)
    conn.close()
"""