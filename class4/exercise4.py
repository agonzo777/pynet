#1/usr/bin/env python

import pexpect
import time

username = 'pyclass'
password = '88newclass'
ip_addr = '50.76.53.27'
port = 8022


rc = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
rc.timeout = 3
rc.expect('ssword:')
rc.sendline(password)
rc.expect('#')
print rc.before
print rc.after
rc.sendline('config t')
rc.expect('#')
print rc.before
print rc.after
rc.sendline('logging buffered 7000')
rc.expect('#')
rc.sendline('end')
rc.expect('#')
print rc.before
print rc.after





