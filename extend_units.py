# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:18:51 2015

@author: bling
"""

import sys
import pytz
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from track_functions import get_drifter,get_fvcom,get_roms,draw_basemap,uniquecolors,clickmap, points_between, points_square,extend_units,totdis
from matplotlib import animation

def extend_units(point, unit, num):
    '''point = (lat,lon); length: units is decimal degrees.
       return a squre points(lats,lons) on center point'''
    (lat,lon) = point; 
    lats=[]; lons=[]
    #unit = unit
    leh = unit*num
    
    #ps = np.mgrid[lat-leh:lat+leh+1:2j, lon-leh:lon+leh+1:2j]; print ps
    #ps = ps*unit
    lts = np.arange(lat-leh,lat+leh+unit,unit); lns = np.arange(lon-leh,lon+leh+unit,unit)
    llp = np.meshgrid(lts,lns); #print llp
    lats.extend(llp[0].flatten()); lons.extend(llp[1].flatten())

    return lats,lons
centerpoint = (41.9,-70.26); unit = 0.04; number = 3
st_lat,st_lon = extend_units(centerpoint,unit,number)
print st_lat,st_lon
points = {'lats':[],'lons':[]}  # collect all points we've gained
points['lats'].extend(st_lat); points['lons'].extend(st_lon)
#points['lats'].extend(latc); points['lons'].extend(lonc)
fig = plt.figure() #figsize=(16,9)
ax = fig.add_subplot(111)
draw_basemap(fig, ax, points)
ax.plot(st_lon,st_lat,'bo')
plt.show()
