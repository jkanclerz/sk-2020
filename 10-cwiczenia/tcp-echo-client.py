#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode(sys.argv[1]))
    #data = s.recv(1024)

#print('Received', repr(data))
