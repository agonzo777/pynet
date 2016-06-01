#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler


net_devices = NetworkDevice.objects.all()
net_devices

creds = Credentials.objects.all()
creds

def main ():
    
    newdev1 = NetworkDevice(device_name='rtr3',device_type='Brocade',ip_address='10.1.1.1',port=22)
    newdev1.save()


    newdev2 = NetworkDevice.objects.get_or_create(device_name='rtr4',device_type='cisco_ios',ip_address='10.2.2.2',port=22)


    

   

if __name__ == "__main__": main()


