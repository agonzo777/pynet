#!/usr/bin/env python

import pexpect
import time
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

rc = ConnectHandler(**pynet2)
rc.config_mode()
output = rc.find_prompt()
print output
output = rc.check_config_mode()
print output


