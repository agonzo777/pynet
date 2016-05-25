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


pynet-sw3 = pyeapi.connect_to('pynet-sw3')

pynet-sw3.enable('show version')



