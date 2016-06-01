#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler


net_devices = NetworkDevice.objects.all()
net_devices

creds = Credentials.objects.all()
creds

def main ():

    for a_device in net_devices:
        if 'pynet-sw' in a_device.device_name:
            a_device.vendor = 'Arista'
        elif 'juniper' in a_device.device_name:
            a_device.vendor = 'Juniper'
        else: 
            a_device.vendor = 'Cisco'
        a_device.save()


   

if __name__ == "__main__": main()


