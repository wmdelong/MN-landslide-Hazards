# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:54:41 2018

@author: Whitney DeLong
"""

# This script is used to pull DEM tiles that exist within DEM_MN.gdb (all tiles within state boundary) into individual AOI geodatabases based on their existence in a given AOI list. 

# Import Modules
import arcpy
from arcpy import env

# Set environments
env.workspace = "I:\Openness"
env.overwriteOutput = True
out_workspace1 = "I:\GDBs\Metro\Openness.gdb"
out_workspace2 = "I:\GDBs\Northeast\Openness.gdb"
out_workspace3 = "I:\GDBs\RedRiver\Openness.gdb"
out_workspace4 = "I:\GDBs\MNRiver\Openness.gdb"
out_workspace5 = "I:\GDBs\Southeast\Openness.gdb"

# Check out 3D Analyst and Spatial Analyst licenses
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("Spatial")

# This creates lists of all tiles within EACH AOI from text file. 
DEM_Metro = open("I:\RasterMosaic\DEM_Metro_FeatureList.txt").readlines() 
DEM_Northeast = open("I:\RasterMosaic\DEM_Northeast_FeatureList.txt").readlines()
DEM_RedRiver = open("I:\RasterMosaic\DEM_RedRiver_FeatureList.txt").readlines()
DEM_MNRiver = open("I:\RasterMosaic\DEM_MNRiver_FeatureList.txt").readlines()
DEM_Southeast = open("I:\RasterMosaic\DEM_Southeast_FeatureList.txt").readlines()

# The following loops copy the rasters from DEM_MN.gdb (GDB containing all DEM tiles) to individual AOI GDBs.  

# This moves DEMs from DEM_MN.gdb to Metro gdb
for fn in DEM_Metro:
   
    infile = fn [:-1] 
   
    outfile = fn [:-1] 
    
    outraster=out_workspace1+"\\"+outfile
    
    outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float",)

# This moves DEMs from DEM_MN.gdb to Northeast gdb
for fn in DEM_Northeast:

    infile = fn[:-1]  
   
    outfile = fn[:-1] 
        
    outraster=out_workspace2+"\\"+outfile
   
    outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float",)

# This moves DEMs from DEM_MN.gdb to Red River gdb  
for fn in DEM_RedRiver:
    
    infile = fn[:-1]  
   
    outfile = fn[:-1] 
    
    outraster=out_workspace3+"\\"+outfile
   
    outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float",)
   
# This moves DEMs from DEM_MN.gdb to MN River gdb
for fn in DEM_MNRiver:
   
    infile = fn[:-1] 
   
    outfile = fn[:-1] 
    
    outraster=out_workspace4+"\\"+outfile
   
    outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float",)
    
# This moves DEMs from DEM_MN.gdb to Southeast gdb
for fn in DEM_Southeast:
   
    infile = fn[:-1]  
   
    outfile = fn[:-1]
    
    outraster=out_workspace5+"\\"+outfile
   
    outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float",)
   
