#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


def myreceive(sock, msglen):

    msg = ''

    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg += str(chunk)

    return msg


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # создаём сокет
s.bind(('0.0.0.0', 2222))
s.listen(10)    # Для созданного сокета включаем режим прослушивания

while True:
    conn, addr = s.accept()     # Принимаем подключение
    print(addr)
    while True:
        data = conn.recv(1024)  # получаем малыми порциями данные от клиента
        print(data.decode('utf8'))
        # data = myreceive(conn, 1024)
        # print(str(data).decode('utf8'))
        if not data:
            break
        if data.decode('utf8') == 'close':
            conn.close()
            break
        # conn.send(data.upper())
        conn.send(data)
    conn.close()