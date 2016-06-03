#!/usr/bin/env/ python

import jsonrpclib
from pprint import pprint as pp
import pyeapi


#ip = '50.76.53.27'
#port = '8443'
#username = 'eapi'
#password = 'ZZteslaX'
#switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)
#switch_url = switch_url + '/command-api'


py3 = pyeapi.connect_to('pynet-sw3')

output = py3.enable('show interfaces')
intf = output[0]
intf = intf['result']
intf = intf['interfaces']



for k,v in intf.items():
#    print "Interface: \n {}".format(k)
    print k
    if k != 'Vlan1':
        counters = v['interfaceCounters']
        print "InOctets: {}".format(counters.get('inOctets'))
        print "OutOctets: {}".format(counters.get('outOctets'))
    else:
        print "Not Applicable"



