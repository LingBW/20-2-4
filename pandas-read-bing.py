# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:54:57 2015

@author: bling
"""

import pandas as pd
from dateutil.parser import parse

data = pd.read_csv('RawData0715_new.txt',sep='|',parse_dates=True)
data = data.dropna(how='all') #drop rows that are all NA
#sort by the values in one or more columns.
data = data.sort_index(by=['Inspector','InspectionDate','InspectionTime']) 
for i in xrange(len(data['InspectionDate'])):
    data['InspectionDate'][i]=parse(data['InspectionDate'][i]).strftime('%m/%d/%Y %H:%M:%S')
names = set(data['Inspector'])
for i in names:
    #index = np.where(data['Inspector']=i)
    indiv = data[data['Inspector']==i]
    indiv.to_csv(i+'.txt',index=False,sep='|')
#print indiv