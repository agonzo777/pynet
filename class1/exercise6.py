#!/usr/bin/env/python

import json
import yaml
from pprint import pprint as pp

list1 = ['strings','integers','booleans','floats']
list1.append({})
list1[-1]['Key1'] = 'Value1'
list1[-1]['Key2'] = 'Value2'

with open('exercise6.yml','w') as f:
    f.write(yaml.dump(list1,default_flow_style=False))

with open('exercise6.yml','r') as a:
   newlist = yaml.load(a)

pp(newlist)


jlist = jason.dumps(list1)


with open('exercise6.json','w') as fhandle:
    jason.dump(jlist,fhandle)

with open('exercise6.json','r') as fhandle:
    new_jlist = jason.load(fhandle)

pp(jlist)


