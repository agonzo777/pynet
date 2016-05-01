#!/usr/bin/env/ python

import paramiko
import time
import pexpect

username = 'pyclass'
password = '88newclass'
port = 8022
ip_addr = '50.76.53.27'

rc = pexpect.spawn('ssh -l {} {} -p {}'.format(username,ip_addr,port))
rc.timeout = 3
rc.expect('ssword:')
rc.sendline(password)
rc.expect('#')
rc.before
rc.after
rc.sendline("show ip int brief")
rc.expect('#')
print rc.before
print rc.after

