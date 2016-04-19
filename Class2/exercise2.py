#!/usr/bin/env/python


import telnetlib
import time

username = 'pyclass'
password = '88newclass'
ip_add = '50.76.53.27'
telnet_port = 23
telnet_to = 6

telnet_handle = telnetlib.Telnet(ip_add,telnet_port,telnet_to)
output = telnet_handle.read_until("sername:", telnet_to)
print output
telnet_handle.write(username + '\n')
output = telnet_handle.read_until('password:',telnet_to)
print output
telnet_handle.write(password + '\n')
output = telnet_handle.read_very_eager()
print output
time.sleep(1)
telnet_handle.write('term len 0' + '\n')
time.sleep(1)
output = telnet_handle.read_very_eager()
telnet_handle.write('show ip int brief'+ '\n')
time.sleep(2)
output = telnet_handle.read_very_eager()

print output


