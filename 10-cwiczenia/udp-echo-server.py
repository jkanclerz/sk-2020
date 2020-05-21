#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, client_address = s.recvfrom(1024)
        if not data:
          break
        print("recieved {}".format(data))
        #sent = s.sendto(data, client_address)

