#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
import time
from multiprocessing import Process, current_process

def show_version(a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,ip=a_device.ip_address,username=creds.username,password=creds.password,port=a_device.port)
    print '#' * 20 + 'SHOW VERSION OUTPUT' + '#'* 20
    print '\n'
    print remote_conn.send_command_expect("show version")
    print
    print '#' * 60

    
def main():
    django.setup()
    
    devices = NetworkDevice.objects.all()
    starttime = datetime.now()
    print 'Start time: ', starttime
    procs = []
    
    for a_device in devices:
        my_proc = Process(target=show_version, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)
    
    for a_proc in procs:
        print a_proc
        a_proc.join()
 
    endtime = datetime.now() - starttime
    print 'Elapsed time: ', endtime














if __name__ == '__main__': main()

