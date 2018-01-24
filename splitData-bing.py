# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:21:46 2015

@author: bling
"""
# read txt file
f = open('RawData0715_new.txt', 'r')
x = f.readlines()
#print x[1]

# turn txt file to list
tot = []
for i in x[1:]:
    #print i.strip()
    if i.strip():
        tot.append(i.strip())
#print tot

Inspector=[]; TempDate=[]; InspectionDate=[]; RecordNum=[]; InspectionTime=[]; 
VehicheID=[]; Location=[]; Street=[]; City=[]; Zip=[]
for i in tot:
    t = i.split('|')
    #print t 
    Inspector.append(t[0]); TempDate.append(t[1]); RecordNum.append(t[2])
    VehicheID.append(t[4]); Location.append(t[5])
    Street.append(t[6]); City.append(t[7]); Zip.append(t[8])
#print Inspector
r=set(Inspector)
#print len(r)
for i in TempDate:
    tu = i.split(' ')
    #print tu
    InspectionDate.append(tu[0]); InspectionTime.append(tu[1])

tou=[]
for i in xrange(len(Inspector)):
    info= Inspector[i]+'|'+InspectionDate[i]+'|'+InspectionTime[i]+'|'+RecordNum[i]+'|'+VehicheID[i]+'|'+Location[i]+'|'+Street[i]+'|'+City[i]+'|'+Zip[i]
    tou.append(info)
#print tou

for i in r:
    files=open(i,'w')
    files.write('Inspector|InspectionDate|InspectionTime|RecordNum|VehicheID|Location|Street|City|Zip\n')
    for k in tou:
        if k.find(i) != -1:
            files.write(k+'\n')
    files.close()
    

    
