# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:54:41 2018

@author: Whitney DeLong

This script is used to pull openness tiles that exist in OpennessGrids folder (all tiles within state boundary) 
into individual AOI geodatabases based on their existence in a given AOI list.
""" 

# Import Modules
import arcpy
from arcpy import env

# Set environment variables
env.workspace = "I:\OpennessGrids"
env.overwriteOutput = True
arcpy.env.scratchWorkspace = "I:\GDBs\Scratch.gdb"
out_workspace1 = "I:\GDBs\Metro\MetroOpenness.gdb"
out_workspace2 = "I:\GDBs\Northeast\NortheastOpenness.gdb"
out_workspace3 = "I:\GDBs\RedRiver\RedRiverOpenness.gdb"
out_workspace4 = "I:\GDBs\MNRiver\MNRiverOpenness.gdb"
out_workspace5 = "I:\GDBs\Southeast\SoutheastOpenness.gdb"

# Check out 3D Analyst and Spatial Analyst licenses
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("Spatial")

# This creates lists of all tiles within EACH AOI from text file. 
OPEN_Metro = open("I:\RasterMosaic\OPEN_Metro_FeatureList.txt").readlines() 
OPEN_Northeast = open("I:\RasterMosaic\OPEN_Northeast_FeatureList.txt").readlines()
OPEN_RedRiver = open("I:\RasterMosaic\OPEN_RedRiver_FeatureList.txt").readlines()
OPEN_MNRiver = open("I:\RasterMosaic\OPEN_MNRiver_FeatureList_2.txt").readlines()
OPEN_Southeast = open("I:\RasterMosaic\OPEN_Southeast_FeatureList_2.txt").readlines()

# The following loops copy the openness rasters from OpennessGrids (folder containing all grids) to individual AOI GDBs.  

# This moves rasters from OpennessGrids to MetroOpenness.gdb
for fn in OPEN_Metro:
   
      infile = fn [:-1]
      print(infile)
   
      outfile = fn [:-1] 
      print(outfile)
      outfilegdb = outfile [:-4]
      print(outfilegdb)

      outraster=out_workspace1+"\\"+outfilegdb
      print(outraster)
      outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float")

# This moves rasters from OpennessGrids to NortheastOpenness.gdb
for fn in OPEN_Northeast:

      infile = fn [:-1]
      print(infile)
   
      outfile = fn [:-1] 
      print(outfile)
      outfilegdb = outfile [:-4]
      print(outfilegdb)

      outraster=out_workspace2+"\\"+outfilegdb
      print(outraster)
      outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float")

# This moves rasters from OpennessGrids to RedRiverOpenness.gdb
for fn in OPEN_RedRiver:
    
      infile = fn [:-1]
      print(infile)
   
      outfile = fn [:-1] 
      print(outfile)
      outfilegdb = outfile [:-4]
      print(outfilegdb)

      outraster=out_workspace3+"\\"+outfilegdb
      print(outraster)
      outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float")
   
# This moves rasters from OpennessGrids to MNRiverOpenness.gdb
for fn in OPEN_MNRiver:
   
      infile = fn [:-1]
      print(infile)
   
      outfile = fn [:-1] 
      print(outfile)
      outfilegdb = outfile [:-4]
      print(outfilegdb)

      outraster=out_workspace4+"\\"+outfilegdb
      print(outraster)
      outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float")
    
# This moves rasters from OpennessGrids to SoutheastOpenness.gdb
for fn in OPEN_Southeast:
   
      infile = fn [:-1]
      print(infile)
   
      outfile = fn [:-1] 
      print(outfile)
      outfilegdb = outfile [:-4]
      print(outfilegdb)

      outraster=out_workspace5+"\\"+outfilegdb
      print(outraster)
      outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float")
