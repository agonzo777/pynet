#!/usr/bin/env/ python

import paramiko
import time

username = 'pyclass'
password = '88newclass'
port = 8022

ip_addr = '50.76.53.27'

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False,port=port)

rc = remote_conn_pre.invoke_shell()
time.sleep(2)
rc.send("terminal length 0\n")
time.sleep(2)
output = rc.recv(6000)
time.sleep(2)
rc.send("config t\n")
time.sleep(2)
rc.send("logging buffered 10000")
time.sleep(2)
output = rc.recv(6000)
print output
rc.send("end")
time.sleep(2)
output = rc.recv(6000)
print output






