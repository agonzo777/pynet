#!/usr/bin/env/python


import telnetlib
import time

username = 'amiri'
password = '1234'
ip_add = '1.2.3.4'
telnet_port = 8124
telnet_to = 6

telnet_handle = telnetlib.Telnet(ip_add,telnet_port,telnet_to)
telnet_handle.read_until("username:", telnet_to)
telnet_handle.write(username,telnet_to)
telnet_handle.read_until('password:',telnet_to)
telnet_handle.write(password,telnet_to)

telnet_handle.read_until('#',telnet_to)
telnet_handle.write('term len 0',telnet_to)
time.sleep(3)
telnet_handle.write('show ip int brief',telnet_to)
output = telnet_handle.read_very_eager()

print output


