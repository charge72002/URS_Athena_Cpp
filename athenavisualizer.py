#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:45:42 2022

@author: Sherry Wong
"""
filedirectory = "/Users/bwong/URS_Athena_Cpp/SWONG_shock_tube_bump_HDF5"
pwd = "/Users/bwong/URS_Athena_Cpp" 
saveDirectory = pwd + "/gifs"

import csv
import sys
import matplotlib as plt
import os
from moviepy.editor import ImageSequenceClip
import shutil

#import matplotlib.animation.MovieWriter
import matplotlib.animation as ani
import matplotlib.pyplot as plt

sys.path.insert(0, pwd) #change working directory
import athena_read as ath



#%%
filename = "/Users/bwong/URS_Athena_Cpp/SWONG_shock_tube_bump_HDF5/Sod.out1.00010.athdf"
data = ath.athdf(filename)
print(data.keys())
x = data['x1v']
y = data['rho'][0][0]
plt.plot(x, y)
plt.title("Density (computational units)")
plt.xlabel("density")
plt.ylabel("x position")

#%%

xKey = 'x1v'
yKey = 'rho'
for i in range(0, 125):
    inFile = (("%s/%s.out%1i.%05i.%s") % (pwd,"Sod",1,i,"athdf"))
    data = ath.athdf(filename)
    x = data[xKey]
    y = data[yKey][0][0]
    plt.plot(x, y)

#%%
#https://stackoverflow.com/questions/4092927/generating-movie-from-python-without-saving-individual-frames-to-files
xKey = 'x1v'
yKey = 'combo'

filename = "/Users/bwong/URS_Athena_Cpp/SWONG_shock_tube_bump_HDF5/Sod.out1.00000.athdf"
data = ath.athdf(filename)
print(data.keys())
x = data['x1v']
y = data['rho'][0][0]


fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_aspect('equal')
plt.tight_layout()

im = ax.plot(x, y)


def update_img(n):
    plt.cla() #clear axes
    ax.set_ylim([0, 2.5])
    inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/SWONG_shock_tube_bump_HDF5","Sod",1,n,"athdf"))
    data = ath.athdf(inFile)
    if yKey == "combo":
        x = data[xKey]
        for yKey2 in ['rho', 'press', 'vel1']:
            y = data[yKey2][0][0]
            im = ax.plot(x, y, label=yKey2)
        ax.legend()
    else:
        x = data[xKey]
        y = data[yKey][0][0]
        im = ax.plot(x, y)
        ax.set_ylabel(yKey2)
    ax.set_title(yKey + "(computational units)")
    ax.set_xlabel("x position (cm)")
    return im

#legend(loc=0)
TEMPani = ani.FuncAnimation(fig,update_img,125,interval=1)
writer = ani.writers['ffmpeg'](fps=30)

TEMPani.save(pwd + '/' + yKey+'.mp4',writer=writer,dpi=100)
print("Saved as " + pwd + '/' + yKey+'.mp4')
#return ani

#ani_frame()
