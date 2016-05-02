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


def main():
    rlist = [pynet1, pynet2]

    for router in rlist:
        rtr = ConnectHandler(**router)
        rtr.config_mode()
        rtr.send_config_from_file(config_file='configfile.txt')
        rtr.exit_config_mode()

main()



