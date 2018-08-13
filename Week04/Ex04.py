# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:14:23 2018

@author: huung
"""

import numpy as np
import pandas as pd
import random as rd

ids=[]
for i in range(20):
	ids.append("id"+str(i+1))
rd.shuffle(ids)
S1=pd.Series(ids[:10])
rd.shuffle(ids)
S2=pd.Series(ids[:10])
S3=pd.Series(np.random.randint(-100, 100, 10))
S4=pd.Series(np.random.randint(-100, 100, 10))
df1=pd.DataFrame({"key":S1, "data1":S3})
df2=pd.DataFrame({"key":S2, "data2":S4})
df=pd.merge(df1, df2)