#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler


net_dev = NetworkDevice.objects.all()
net_dev

creds = Credentials.objects.all()
creds

def main ():
    
    lastdev = net_dev[8]
    lastdev.delete()
    lastdev2 = net_dev[7]
    lastdev2.delete()

 

    

   

if __name__ == "__main__": main()


