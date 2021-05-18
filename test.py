#!/usr/bin/python

import sys, socket, time
import PyQt6.QtWidgets as wd
from PyQt6.QtWidgets import QApplication, QWidget
import scapy.all as sm

print("go")

# a=sm.sniff(filter="ip",count=10)

# a.nsummary()

def arp_monitor_callback(pkt):
	print(pkt.summary())
	print("boom")
	print(pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))

sm.sniff(prn= arp_monitor_callback, filter="ip", store=0)