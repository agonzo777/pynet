#!/usr/bin/env python

import netmiko
from netmiko import ConnectHandler

password = '88newclass'

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'port': 8022,
}

juniper_srx = {
   'device_type': 'juniper',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'secret': '',
    'port': 9822,
}

pynet1 = ConnectHandler(**pynet1)
pynet2 = ConnectHandler(**pynet2)
juniper = ConnectHandler(**juniper_srx)

out1 = pynet1.send_command("sh ip arp")
out2 = pynet2.send_command("sh ip arp")
out3 = juniper.send_command("sh arp")

print 'Pynet1:\n' + out1 + '\nPynet2:\n' + out2 + '\nJuniper:\n' + out3



