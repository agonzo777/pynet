#!/usr/bin/env/python


import paramiko
import pysnmp
import my_func
import os
import sys
from pprint import pprint as pp



print 'SNMP Version ', pysnmp.version
print 'Paramiko Version ', paramiko.__version__

my_func.hello()


print pp(sys.path)



