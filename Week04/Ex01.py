# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 10:26:31 2018

@author: huung
"""
import pandas as pd

string = "Ah meta descriptions… the last bastion of traditional marketing! The only cross-over point between marketing and search engine optimisation! The knife edge between beautiful branding and an online suicide note!"
# convert the string to a panda Series
s = pd.Series(string.split())
# create the mask
mask = s.map(lambda x: sum([x.lower().count(i) for i in 'aeuoi']) >=3)
# apply the mask to series
print(s[mask])
