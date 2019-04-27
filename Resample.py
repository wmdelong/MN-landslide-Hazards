# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:43:52 2018

@author: Whitney DeLong
"""

import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True

# Set environments
env.workspace = "I:\GDBs\DEM_MN.gdb"
out_workspace1 = "I:\GDBs\Metro\METRO_DEM_1x1m.gdb"
out_workspace2 = "I:\GDBs\Northeast\Northeast_DEM_1x1m.gdb"
out_workspace3 = "I:\GDBs\RedRiver\RedRiver_DEM_1x1m.gdb"
out_workspace4 = "I:\GDBs\MNRiver\MNRiver_DEM_1x1m.gdb"
out_workspace5 = "I:\GDBs\Southeast\Southeast_DEM_1x1m.gdb"

# This creates lists of all tiles within EACH AOI from text file. 
DEM_Metro = open("I:\RasterMosaic\DEM_Metro_FeatureList.txt").readlines() 
DEM_Northeast = open("I:\RasterMosaic\DEM_Northeast_FeatureList.txt").readlines()
DEM_RedRiver = open("I:\RasterMosaic\DEM_RedRiver_FeatureList.txt").readlines()
DEM_MNRiver = open("I:\RasterMosaic\DEM_MNRiver_FeatureList.txt").readlines()
DEM_Southeast = open("I:\RasterMosaic\DEM_Southeast_FeatureList.txt").readlines()

# The following loops resample DEMs within each study area list to 1x1 m resolution and saves them to the corresponding updated gdb.

# Resample DEMs in Metro study area to 1x1 m, move to corresponding gdb.
for fn in DEM_Metro:
   
    inFile = fn [:-1] 
   
    outFile = fn [:-1] 
    
    outRaster=out_workspace1+"\\"+outFile
    
    outResample = arcpy.Resample_management(inFile, outRaster, "1", "BILINEAR") 

# Resample DEMs in Northeast study area to 1x1 m, move to corresponding gdb.    
for fn in DEM_Northeast:
   
    inFile = fn [:-1] 
   
    outFile = fn [:-1] 
    
    outRaster=out_workspace2+"\\"+outFile
    
    outResample = arcpy.Resample_management(inFile, outRaster, "1", "BILINEAR") 
    
# Resample DEMs in Red River study area to 1x1 m, move to corresponding gdb.
for fn in DEM_RedRiver:
   
    inFile = fn [:-1] 
   
    outFile = fn [:-1] 
    
    outRaster=out_workspace3+"\\"+outFile
    
    outResample = arcpy.Resample_management(inFile, outRaster, "1", "BILINEAR") 

# Resample DEMs in MN River study area to 1x1 m, move to corresponding gdb.    
for fn in DEM_MNRiver:
   
    inFile = fn [:-1] 
   
    outFile = fn [:-1] 
    
    outRaster=out_workspace4+"\\"+outFile
    
    outResample = arcpy.Resample_management(inFile, outRaster, "1", "BILINEAR") 
    
# Resample DEMs in Southeast study area to 1x1 m, move to corresponding gdb.
for fn in DEM_Southeast: 
   
    inFile = fn [:-1] 
   
    outFile = fn [:-1] 
    
    outRaster=out_workspace5+"\\"+outFile
    
    outResample = arcpy.Resample_management(inFile, outRaster, "1", "BILINEAR") 
