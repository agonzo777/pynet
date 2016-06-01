#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django


def main():
    django.setup()
    
    devices = NetworkDevice.objects.all()
    starttime = datetime.now()
    print 'Start time: ', starttime
    for a_device in devices:
        device_type = a_device.device_type
        port = a_device.port
        secret = ''
        ip = a_device.ip_address
        creds = a_device.credentials
        username = creds.username
        password = creds.password
        remote_conn = ConnectHandler(device_type=device_type,ip=ip,username=username,password=password,port=port)
        print '#' * 20 + 'SHOW VERSION OUTPUT' + '#'* 20
        print '\n'
        print remote_conn.send_command_expect("show version")
        print 
        print '#' * 60
    endtime = datetime.now() - starttime
    print 'End time: ', endtime














if __name__ == '__main__': main()

