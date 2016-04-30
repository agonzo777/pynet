import snmp_helper
from pprint import pprint as pp
import yaml
import json
import pysnmp
import email_helper
import smtplib
import pygal

snmp_oids = (('ccmHistoryRunningLastChanged','1.3.6.1.4.1.9.9.43.1.1.1.0',True),('ccmHisotryRunningLastSaved','1.3.6.1.4.1.9.9.43.1.1.2.0',True),('ccmHistoryStartupLastCHanged','1.3.6.1.4.1.9.9.43.1.1.3.0',True))

username = 'pysnmp'
auth_key = 'galileo1'
encrypt_key ='galileo1'

snmp_user = (username,auth_key,encrypt_key)

device = '50.76.53.27'
snmp_port = 8061

snmp_device = (device, snmp_port)

snmp_data = snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=snmp_oids[0][1])
runtime  = int(snmp_helper.snmp_extract(snmp_data))

changeoccured = False


while (changeoccured != True):
    snmp_data = snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=snmp_oids[0][1])
    output = int(snmp_helper.snmp_extract(snmp_data))
    if output > runtime:
        diff = int(output) - runtime
        recipient = 'amiri.gonzalez@gmail.com'
        subject = 'Change Occured'
        message = 'A change occured %d' % diff
        sender = 'amiri.gonzalez@gmail.com'
        email_helper.send_mail(recipient, subject, message, sender)
        changeoccured = True
    else:
        continue









