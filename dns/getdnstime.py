# -*- coding:utf-8 -*-
import socket
import csv
import sys
from timeit import timeit
class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
def send():
    sock_recv = 0
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(msg, ('114.114.114.114', 53))
    sock_recv = sock.recv(4096)
    while True:
        if sock_recv != 0:
            break

def getlineNum():
    f = open(u"website.txt", 'r')
    content = csv.reader(f)
    lineNum = 0
    for line in content:
        lineNum += 1
    f.close()
    return (lineNum)  # lineNum就是你要的文件行数
def creatXC():
    f = open(u"website.txt", 'r')
    for i in range(0,10):
        line = f.readline()
        print line
        split1(line)

def split1(line):
    global msg
    st1 = line.split('.')
    num = len(st1[1])
    if num == 2:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x02%s\x03com\x00\x00\x01\x00\x01' % (st1[0], st1[1])
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)
    if num == 3:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x03%s\x03com\x00\x00\x01\x00\x01' % (
        st1[0], st1[1])
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)
    if num == 4:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x04%s\x03com\x00\x00\x01\x00\x01' % (
            st1[0], st1[1])
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)
    if num == 5:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x05%s\x03com\x00\x00\x01\x00\x01' % (
        st1[0], st1[1],)
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)
    if num == 6:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x06%s\x03com\x00\x00\x01\x00\x01' % (
            st1[0], st1[1])
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)
    if num == 7:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x07%s\x03com\x00\x00\x01\x00\x01' % (
            st1[0], st1[1])
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)
    if num == 8:
        msg = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03%s\x08%s\x03com\x00\x00\x01\x00\x01' % (
            st1[0], st1[1])
        for i in range(11):
            t = timeit('send()', 'from __main__ import send', number=1)
            print(t)

sys.stdout = Logger(u"output.txt")  
creatXC()
