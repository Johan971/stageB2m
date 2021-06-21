#!/usr/bin/python

import sys, socket, time
import PyQt6.QtWidgets as wd
from PyQt6.QtWidgets import QApplication, QWidget
import scapy.all as sm
import os,shutil,time
print("go")

# a=sm.sniff(filter="ip",count=10)

# a.nsummary()
def arp_monitor_callback(pkt):
	# print(pkt.summary())
	print("boom")
	# print(pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
	# print(pkt.sprintf("{Ethernet:%Ether.src% IP:%IP.src% -> %IP.dst% %Ether.dst%\n}"))
	# print(pkt.sprintf("Source : {%Ether.src% %IP.src% -> %IP.dst% %Ether.dst%\n}"))

	print(pkt.sprintf("Source :: Ether:%Ether.src% IP:%IP.src% =======> Destination :: Ether:%Ether.dst% IP:%IP.dst%"))
	# print(pkt.sprintf("Source: {pkt.src}\tDestination: {pkt.dst}"))

	# pkt.show2()
	# pkt.decode_payload_as("str")
	# object_methods = [method_name for method_name in dir(pkt) ]
	# print(object_methods)


# sm.sniff(prn= arp_monitor_callback, filter="ip", store=0)

sm.sniff(prn= arp_monitor_callback,filter = 'dst port 12005')

pktMethods=['_PickleType', '__all_slots__', '__bool__', '__bytes__', '__class__', '__class_getitem__', '__contains__', '__deepcopy__',
'__delattr__', '__delitem__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__',
'__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__iterlen__', '__le__', '__len__', '__lt__', '__module__', '__mul__',
'__ne__', '__new__', '__nonzero__', '__orig_bases__', '__parameters__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__rtruediv__',
'__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__truediv__', '__weakref__', '_answered',
'_defrag_pos', '_do_summary', '_is_protocol', '_name', '_overload_fields', '_pkt', '_resolve_alias', '_show_or_dump', '_superdir', 'add_payload',
'add_underlayer', 'aliastypes', 'answers', 'build', 'build_done', 'build_padding', 'build_ps', 'canvas_dump', 'class_default_fields', 'class_default_fields_ref',
'class_dont_cache', 'class_fieldtype', 'class_packetfields', 'clear_cache', 'clone_with', 'command', 'convert_packet', 'convert_packets', 'convert_to', 'copy', 
'copy_field_value', 'copy_fields_dict', 'decode_payload_as', 'default_fields', 'default_payload_class', 'delfieldval', 'deprecated_fields', 'direction',
'dispatch_hook', 'display', 'dissect', 'dissection_done', 'do_build', 'do_build_payload', 'do_build_ps', 'do_dissect', 'do_dissect_payload',
'do_init_cached_fields', 'do_init_fields', 'dst', 'explicit', 'extract_padding', 'fields', 'fields_desc', 'fieldtype', 'firstlayer', 'fragment',
'from_hexcap', 'get_field', 'getfield_and_val', 'getfieldval', 'getlayer', 'guess_payload_class', 'hashret', 'haslayer', 'hide_defaults', 'init_fields',
'iterpayloads', 'lastlayer', 'layers', 'lower_bonds', 'match_subclass', 'mysummary', 'name', 'original', 'overload_fields', 'overloaded_fields',
'packetfields', 'payload', 'payload_guess', 'pdfdump', 'post_build', 'post_dissect', 'post_dissection', 'post_transforms', 'pre_dissect',
'prepare_cached_fields', 'psdump', 'raw_packet_cache', 'raw_packet_cache_fields', 'remove_payload', 'remove_underlayer', 'route', 'self_build',
'sent_time', 'setfieldval', 'show', 'show2', 'show_indent', 'show_summary', 'sniffed_on', 'sprintf', 'src', 'summary', 'svgdump', 'time', 'type',
'underlayer', 'update_sent_time', 'upper_bonds', 'wirelen']