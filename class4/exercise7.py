#!/usr/bin/env python

from netmiko import ConnectHandler
import netmiko

password = '88newclass'

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'port': 8022,
}

py2 = ConnectHandler(**pynet2)
py2.config_mode()
py2.send_command("logging buffered 8888")
py2.exit_config_mode()

