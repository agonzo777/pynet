import json
import yaml
from ciscoconfparse import CiscoConfParse

cryptofile = CiscoConfParse("cisco_ipsec.txt")

headcrypt = cryptofile.find_objects_w_child(parentspec=r"crypto map CRYPTO",childspec=r"set pfs group2")


for line in range(len(headcrypt)):
    print headcrypt[line].text
    parent = headcrypt[line]
    for child in parent.children:
        print child.text


