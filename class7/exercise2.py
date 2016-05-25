#!/usr/bin/env python

import pyeapi
from pprint import pprint as pp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="used to create a vlan with the name here")
parser.add_argument("vlan", type=int)
parser.add_argument("--remove", help="Remove vlan", action="store_true")
args = parser.parse_args()


pynetsw3 = pyeapi.connect_to('pynet-sw3')
vlanapi = pynetsw3.api('vlans')
vlanapi.autorefresh = True

if args.name:
    vname = args.name
    vid = args.vlan
    if vlanapi.get(vid):
        print "Vlan {} already exists".format(vid)
    print ('\nCreating Vlan {}'.format(vid))
    vlanapi.create(vid)
    print 'Setting vlan {} name to {}'.format(vid,vname)
    vlanapi.set_name(vid, vname)
if args.remove:
    if vlanapi.get(args.vlan):
        print 'Deleting vlan {}'.format(args.vlan)
        vlanapi.delete(args.vlan)
    else: 
        print 'Vlan {} does not exist'.format(args.vlan)


 


