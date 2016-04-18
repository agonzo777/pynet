#!/usr/bin/env/python

import os
import sys
import pysnmp
from snmp_helper import snmp_get_oid,snmp_extract

comm_string = 'galileo'
snmprtr1 = 7961
snmprtr2 = 8061
rtr_ip = '50.76.53.27'
router_snmps = (snmprtr1,snmprtr2)
oid_desc = '1.3.6.1.2.1.1.1.0'
oid_name = '1.3.6.1.2.1.1.5.0'
oids = (oid_desc, oid_name)

for snmp_port  in router_snmps:
    for oid in oids:
        device = (rtr_ip,comm_string,snmp_port)
        getoid = snmp_get_oid(device, oid)
        output = snmp_extract(getoid)
        print output

   

