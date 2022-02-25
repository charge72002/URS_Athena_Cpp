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
import numpy as np

#import matplotlib.animation.MovieWriter
import matplotlib.animation as ani
import matplotlib.pyplot as plt

sys.path.insert(0, pwd) #change working directory
import athena_read as ath



#%%
filename = "/Users/bwong/URS_Athena_Cpp/SWONG_shock_tube_bump_HDF5_res512/Sod.out1.00000.athdf"
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

#%% BIIG plotting
#https://stackoverflow.com/questions/4092927/generating-movie-from-python-without-saving-individual-frames-to-files
xKey = 'x1v'
#xKey = 'x1v x=x[0:256]'
yKey = 'combo'
trim = [0, 256] #trim by index
maxT = 125

data = ath.athdf(filename)
print(data.keys())
x = data['x1v']
y = data['rho'][0][0]

#do this only once for time efficiency
#x = None
x = data[xKey]
if trim!= None: x, y = x[trim[0]:trim[1]], y[trim[0]:trim[1]]

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_aspect('equal')
plt.tight_layout()
im = ax.plot(x, y)

def update_img(n):
    time = 0
    plt.cla() #clear axesx
    ax.set_ylim([0, 2.5])
    inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/SWONG_shock_tube_bump_HDF5_res512","Sod",1,n,"athdf"))
    data = ath.athdf(inFile)
    
    #plot y fields
    if yKey == "combo":
        for yKey2 in ['rho', 'press', 'vel1']:
            y = data[yKey2][0][0]
            if trim!= None: y=y[trim[0]:trim[1]]
            im = ax.plot(x, y, label=yKey2)
        #plot just temp, special
        y = data["press"][0][0]/data["rho"][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]
        im = ax.plot(x, y, label="temp")
        ax.legend()
    elif yKey == "temp":
        y = data["press"][0][0]/data["rho"][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]
        im = ax.plot(x, y)
        ax.set_ylabel(yKey)
    else:
        y = data[yKey][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]
        im = ax.plot(x, y)
        ax.set_ylabel(yKey)
    ax.set_title(yKey + "(computational units) t=" + str(n))
    ax.set_xlabel("x position (cm)")
    time+=1;
    return im

#legend(loc=0)
TEMPani = ani.FuncAnimation(fig,update_img,maxT,interval=1)
writer = ani.writers['ffmpeg'](fps=30)

saveFile = pwd + '/' + yKey+'_res512.mp4'
TEMPani.save(saveFile,writer=writer,dpi=100)
print("Saved as " + saveFile)
#return ani

#ani_frame()

#%%
###################
# CONVERGENCE STUDY
###################

#https://stackoverflow.com/questions/4092927/generating-movie-from-python-without-saving-individual-frames-to-files
xKey = 'x1v'
yKey = 'combo'
# fileStrings = [
#     "res128", 
#     "res256",
#     "res512",
#     "res1024",
#     "res2048"]

fileStrings = [
    "res2048", 
    "res1024",
    "res512",
    "res256",
    "res128"]

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
    for string in fileStrings:
        inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/SWONG_shock_tube_bump_HDF5_"+string,"Sod",1,n,"athdf"))
        data = ath.athdf(inFile)
        x = data[xKey]
        y = data['rho'][0][0]
        im = ax.plot(x, y, ".", label=string)
    ax.legend()
    ax.set_title(yKey + "(computational units)")
    ax.set_xlabel("x position (cm)")
    ax.hlines(1.4, max(data[xKey]), min(data[xKey]), linestyles='dashed')
    return im

#legend(loc=0)
TEMPani = ani.FuncAnimation(fig,update_img,125,interval=1)
writer = ani.writers['ffmpeg'](fps=30)

TEMPani.save(pwd + '/' + yKey+'_Convergence2.mp4',writer=writer,dpi=250)
print("Saved as " + pwd + '/' + yKey+'.mp4')
#return ani

#ani_frame()

