#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials

net_devices = NetworkDevice.objects.all()
net_devices

creds = Credentials.objects.all()
creds

def main ():
    std_cred = creds[0]
    sw_cred = creds[1]

    for a_device in net_devices:
        if 'pynet-sw' in a_device.device_name:
            a_device.credentials = sw_cred
        else:
            a_device.credentials = std_cred
        a_device.save()


    


    




    

if __name__ == "__main__": main()


