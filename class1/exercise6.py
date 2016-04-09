#!/usr/bin/env/python


import yaml


list1 = ['strings','integers','booleans','floats']
list1.append({})
list1[-1]['Key1'] = 'Value1'
list1[-1]['Key2'] = 'Value2'

with open('exercise6.yml','w') as f:
    f.write(yaml.dump(list1,default_flow_style=False))


