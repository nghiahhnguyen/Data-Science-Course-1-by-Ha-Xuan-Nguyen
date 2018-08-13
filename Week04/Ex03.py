# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 21:49:08 2018

@author: huung
"""

import pandas as pd
import numpy as np
data={"month":pd.date_range(start="2018-01-31", freq='M', periods=50), "sale":pd.Series(np.random.randint(10, 30, 50))}
df=pd.DataFrame(data)
df["year"]=[str(d.year) for d in df["month"]]
df.sale.groupby(df.year).sum()