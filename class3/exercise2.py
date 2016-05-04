import pysnmp
import snmp_helper
import pygal
import time


username = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

snmp_user = (username, auth_key, encrypt_key)

device = '50.76.53.27'
snmp_port = 7961

snmp_device = (device, snmp_port)

snmp_oids = (
('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)

minperhour = 60
running = True

inoctets = []
outoctets = []
inucast = []
outucast = []

baseinoctet = ''
baseoutoctet = ''
baseinucast = ''
baseoutucast = ''


#Obtain Base Value of Interface to have a starting point
for dev, snmp_oid in snmp_oids:
    if dev.startswith('ifDes'):
        continue
    else:
        snmp_data = snmp_helper.snmp_get_oid_v3(snmp_device,snmp_user,oid=snmp_oid)
        if dev.startswith('ifInOctet'):
            baseinoctet = int(snmp_helper.snmp_extract(snmp_data))
            print "Baseinoctet: ", baseinoctet
        elif dev.startswith('ifInUcast'):
            baseinucast = int(snmp_helper.snmp_extract(snmp_data))
            print "BaseInUCast: ", baseinucast
        elif dev.startswith('ifOutOctet'):
            baseoutoctet = int(snmp_helper.snmp_extract(snmp_data))
            print "BaseOutOctet: ", baseoutoctet
        elif dev.startswith('ifOutUcast'):
            baseoutucast = int(snmp_helper.snmp_extract(snmp_data))
            print "BaseOutUcast: ", baseoutucast


while running == True:
    time.sleep(300)
    minperhour -= 5
    print minperhour, ' minutes left'
    if minperhour > 0:
        for dev, snmp_oid in snmp_oids:
            if dev.startswith('ifDes'):
                continue    
            else:
                snmp_data = snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=snmp_oid)
                output = int(snmp_helper.snmp_extract(snmp_data))
                if dev.startswith('ifInOctets'):
                    new = output - baseinoctet
                    inoctets.append(new)
                elif dev.startswith('ifInUnicast'):
                    new = output - baseinucast
                    inunicast.append(new)
                elif dev.startswith('ifOutOctets'):
                    new = output - baseoutoctet
                    outoctets.append(new)
                elif dev.startswith('ifOutUcast'):
                    new = output - baseoutucast
                    outucast.append(new)
    
    else:
        running = False


#Create a Chart of Type Line
line_chartA = pygal.Line()
#Chart Title
line_chartA.title = "Input/Output Octets"
#Chart X-Axis Labels
line_chartA.x_labels = ['5','10','15','20','25','30','35','40','45','50','55','60']
#Add the lines to the graphs
line_chartA.add('InOctets',inoctets)
line_chartA.add('OutOctets',outoctets)

#Chart image file
line_chartA.render_to_file('inoutoctets.svg')



#Create a Chart of Type Line
line_chartB = pygal.Line()
#Chart Title
line_chartB.title = "Input/Output Ucast"
#Chart X-Axis Labels
line_chartB.x_labels = ['5','10','15','20','25','30','35','40','45','50','55','60']
#Add the lines to the graphs
line_chartB.add('InOctets',inucast)
line_chartB.add('OutOctets',outucast)

#Chart image file
line_chartB.render_to_file('inoutucast.svg')

print '.svg files have been created'

