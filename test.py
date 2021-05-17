#!/usr/bin/python

import sys, socket
import PyQt6.QtWidgets as wd
from PyQt6.QtWidgets import QApplication, QWidget

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(family,type)

mySocket.bind = (("192.168.1.26", 12006))

# check = mySocket.connect_ex(location)

while True:
    data, addr = mySocket.recvfrom(1024)
    print( addr[1])
 

print(check)