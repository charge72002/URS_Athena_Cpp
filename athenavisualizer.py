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



#%% load file
#filename = "/Users/bwong/URS_Athena_Cpp/SWONG_shock_tube_bump_HDF5_res512/Sod.out1.00000.athdf"
filename = "/Users/bwong/URS_Athena_Cpp/scalar/Sod.out1.00000.athdf"
data = ath.athdf(filename)
print(data.keys())

#%% Plot single field
x = data['x1v']
y = data['rho'][0][0]
plt.plot(x, y)
plt.title("Density (computational units)")
plt.xlabel("density")
plt.ylabel("x position")
    
#inFile = (("%s/%s.out%1i.%05i.%s") % (pwd,"Sod",1,i,"athdf"))
#Format string (THIS IS C VALUE DELIMITING)

#%% BIIG plotting
#https://stackoverflow.com/questions/4092927/generating-movie-from-python-without-saving-individual-frames-to-files
# xKey = 'x1v'
# yKey = 'combo'
# trim = None
# maxT = 125 #default 125

#add custom field(s)
#data['temp'] = data["press"][0][0]/data["rho"][0][0]

xKey = 'x1v'
yKey = 'combo_scalar'
#trim = [0, 256] #trim by index
trim = None
maxT = 125 #default 125

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
    plt.cla() #clear axes
    ax.set_ylim([0, 2.5])
    #WATCH OUT
    inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/scalar","Sod",1,n,"athdf"))
    #inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/SWONG_shock_tube_bump_HDF5_res512","Sod",1,n,"athdf"))
    #inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/LowPres_res512","Sod",1,n,"athdf"))

    data = ath.athdf(inFile)

    #plot y fields
    if yKey == "combo" or yKey == "combo_scalar":
        for yKey2 in ['rho', 'press', 'vel1']:
            y = data[yKey2][0][0]
            if trim!= None: y=y[trim[0]:trim[1]]
            im = ax.plot(x, y, label=yKey2)
        y = data["press"][0][0]/data["rho"][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]    
        im = ax.plot(x, y, label='temp')
    elif yKey == "temp":
        y = data["press"][0][0]/data["rho"][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]    
        im = ax.plot(x, y, label=yKey)
        ax.set_ylabel(yKey) 
    elif yKey != 'r0' and yKey != 'combo_scalar':
        y = data[yKey][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]    
        im = ax.plot(x, y, label=yKey)
        ax.set_ylabel(yKey) 
    if yKey == "r0" or yKey == "combo_scalar":
        y = data['r0'][0][0] * data['rho'][0][0]
        if trim!= None: y=y[trim[0]:trim[1]]    
        im = ax.plot(x, y, label='r0')
        ax.set_ylabel('r0') 
    ax.legend()
    ax.set_title(yKey + "(computational units) t=" + str(n))
    ax.set_xlabel("x position (cm)")
    return im

#legend(loc=0)
TEMPani = ani.FuncAnimation(fig,update_img,maxT,interval=1)
writer = ani.writers['ffmpeg'](fps=30)

saveFile = pwd + '/' + yKey+'_res512.mp4'
TEMPani.save(saveFile,writer=writer,dpi=100)
print("Saved as " + saveFile)
#return ani

#ani_frame()

#%% CONVERGENCE STUDY

#https://stackoverflow.com/questions/4092927/generating-movie-from-python-without-saving-individual-frames-to-files
xKey = 'x1v'
yKey = 'vel1'
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

#if you have a LOT of diferent resolutoins

data = ath.athdf(filename)
print(data.keys())
x = data['x1v']
y = data['press'][0][0]

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
        if(yKey=="temp"):
            data['temp'] = data["press"][0][0]/data["rho"][0][0]
            y = data[yKey]
        else:
            y = data[yKey][0][0]
        im = ax.plot(x, y, label=string)
    ax.set_ylim(0.0, 2.5)
    ax.set_xlim(0.6, 1.2)
    #ax.set_aspect('auto');
    ax.set_aspect(0.6/2.5);
    ax.legend()
    ax.set_title(yKey + "(computational units)" + str(n))
    ax.set_xlabel("x position")
    ax.hlines(1.4, max(data[xKey]), min(data[xKey]), linestyles='dashed')
    return im

#legend(loc=0)
TEMPani = ani.FuncAnimation(fig,update_img,125,interval=1)
writer = ani.writers['ffmpeg'](fps=30)

saveFile = pwd + '/' + yKey+'_Convergence1.mp4'
TEMPani.save(saveFile,writer=writer,dpi=300)
print("Saved as " + saveFile)
#return ani

#ani_frame()

#%% Custom Plotting Fcn

xKey2 = 'x1v'
yKey2 = 'combo'
trim = [0, 256] #trim by index
maxT = 125 #default 125

data = ath.athdf(filename)
print(data.keys())
x = data['x1v']
y = data['rho'][0][0]

#do this only once for time efficiency
#x = None
x = data[xKey2]
if trim!= None: x, y = x[trim[0]:trim[1]], y[trim[0]:trim[1]]

#normally one-time setup
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_aspect('equal')
plt.tight_layout()
im = ax.plot(x, y)

#setup x field; can be cfg to have multiple x?
x = data[xKey2]
if trim!= None: x, y = x[trim[0]:trim[1]], y[trim[0]:trim[1]]

#%% custom plot 1x method
def custom_plot(n, *fargs):
    xKey = fargs[0]
    yKeys = fargs[1]
    print(str(n) + "\txKey: " + str(xKey) + "\tyKeys: " + str(yKeys))
    plt.cla() #clear axes
    ax.set_ylim([0, 2.5])
    #CAREFUL on what file 
    inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/SWONG_shock_tube_bump_HDF5_res512","Sod",1,n,"athdf"))
    #inFile = (("%s/%s.out%1i.%05i.%s") % (pwd+"/LowPres_res512","Sod",1,n,"athdf"))

    data = ath.athdf(inFile)

    #plot y fields
    for yKey in yKeys:
        if yKey == "temp":
            y = data["press"][0][0]/data["rho"][0][0]
            if trim!= None: y=y[trim[0]:trim[1]]
            im = ax.plot(x, y, label=yKey)
            ax.set_ylabel(yKey)
        else:
            y = data[yKey][0][0]
            if trim!= None: y=y[trim[0]:trim[1]]
            im = ax.plot(x, y, label=yKey)
            ax.set_ylabel(yKey)
    ax.legend()
    ax.set_title(yKey + "(computational units) t=" + str(n))
    ax.set_xlabel("x position (cm)")
    plt.show()
    return im
#%%
#legend(loc=0)
TEMPani = ani.FuncAnimation(fig, custom_plot, maxT, interval=1, fargs=(xKey2, ['rho', 'press', 'vel1', 'temp']))
writer = ani.writers['ffmpeg'](fps=30)

saveFile = pwd + '/' + yKey2+'TEST_res512.mp4'
TEMPani.save(saveFile,writer=writer,dpi=100)
print("Saved as " + saveFile)
#return ani

#ani_frame()

#%%
#MAKE SURE TO "unpack the iterable" USING *
trim = [0, 256] #trim by index
custom_plot(30, *('x1v', ['rho', 'press', 'vel1', 'temp']))


#zip("mySring, ", "regex")

#%%
thing = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]