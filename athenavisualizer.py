#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:45:42 2022

@author: Sherry Wong
"""
import csv
import sys
import matplotlib as plt
import os
from moviepy.editor import ImageSequenceClip
import shutil

pwd = os.getcwd()
# if(len(sys.argv)==2):
#     pwd = str(sys.argv[1])
#     print(pwd)
# else:
#     raise Exception("Please provide a working directory containing the .tab files. Use the full directory path or something like $pwd")
saveDirectory = pwd + "/TEMP"
os.mkdir(saveDirectory)
#DANGER!!! The line below removes the directory.
shutil.rmtree(saveDirectory) #delete images to save space

#%% READ .tab
#adapted from EnergyConservation.py

dataDict = {}

pwd = "/Users/bwong/athena/SWONG_shock_tube_test1/"
with open(pwd + 'Sod.block0.out1.00000.tab', 'r', newline='') as file:
    r = csv.DictReader(file)
    linenum=1 #skip first line
    for row in r:
        # print(row.keys())
        for label in row: 
            if(linenum==1): dataDict[label] = [] #init
            dataDict[label].append(float(row[label]))
        linenum+=1
    print(str(linenum) + " lines read.")
    print(dataDict.keys())
#timeStamps = dataDict.pop('t')

#for fileName in sorted(os.listdir(filedirectory)):
#    if(fileName.endswith(".tab")):
    
    
        
#%%
##########
# Make Gif
##########
#https://www.tutorialexample.com/python-create-gif-with-images-using-moviepy-a-complete-guide-python-tutorial/
#taken from Curl_Div_Gifs.py

import moviepy

field = "div"
images = []
for fileName in os.listdir(saveDirectory + '/' + field): #set in initial parameters
    if (fileName.endswith(".png")):#avoid file format errors, even hidden 
        images.append(saveDirectory + '/' + field + '/' + fileName)
#USE GLOB TO ORDER FILES
images = sorted(images)
print(images)
clip = ImageSequenceClip(images, fps=15)
# clip.write_gif(saveDirectory + '/' + field + '.gif') #saves in outside folder
clip.write_videofile(saveDirectory + '/' + field + '.mp4') #save as .mp4

clip.close()
#DANGER!!! The line below removes the directory.
# shutil.rmtree(saveDirectory + '/' + field) #delete images to save space