#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(str.encode(sys.argv[1]), (HOST, PORT))
    #data = s.recv(1024)
    #print('Received', repr(data))
