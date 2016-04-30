import pysnmp
import snmp_helper
import pygal


username = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

snmp_user = (username, auth_key, encrypt_key)

device = '50.76.53.27'
snmp_port = 8061

snmp_device = (device, snmp_port)

snmp_oids = (
('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)

minperhour = 60


while (minperhour > 0):
    for des, each_oid in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=each_oid)
        output = int(snmp_helper.snmp_extract(snmp_data)
        if des == 'ifInOctests_fa4':
            inoctets.append[output]
        if des == 'ifInUnicastPkts_fa4':
            inunicast.append[output]
        if des == 'ifOutOctests_fa4':
            outoctets.append[output]
        if des == 'ifOutUcastPkts_fa4':
            outucast.append[output]
    minperhour -= 5
    time.sleep(300) 







