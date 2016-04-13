import json
import yaml
from ciscoconfparse import CiscoConfParse

cryptofile = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cryptofile.find_objects(r'^crypto map CRYPTO')
for line in crypto_map:
    print line.text


for item in range(len(crypto_map)):
    eachcrypto = crypto_map[item]
    for line in eachcrypto.children:
        print line.text








