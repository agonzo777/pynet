from ciscoconfparse import CiscoConfParse
import yaml
import json
from pprint import pprint as pp


ciscocfg = CiscoConfParse('cisco_ipsec.text')

nonaes = ciscocfg.find_objects_wo_child(parentspec=r'crpto map CRYPTO',childspec=r'set transform-set AES-SHA')

for item in range(len(nonaes)):
    print nonaes[item].text
    cryptemp = nonaes[item]
    for line in cryptemp.children:
        tset = line.text.strip()
        if tset.startswith('set transform-set'):
            print tset


