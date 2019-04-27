# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:48:31 2018

@author: Whitney DeLong
"""

# This script is used to pull DEM tiles within list (within State of Minnesota boundary) and put them into a geodatabase. Original dataset contains many NoData tiles that we do not want in GDB. 

# Import Modules
import arcpy
from arcpy import env

# Set environment
arcpy.env.workspace = "D:\GeoTiffDEM"
arcpy.env.overwriteOutput = True
out_workspace = "I:\GeoTiffDEM_32"

# Check out 3D Analyst and Spatial Analyst licenses
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("Spatial")

# This creates list of all tiles within MN from text file. 
DEMlist = open("I:\RasterMosaic\DEM_MN_FeatureList.txt").readlines()

# This loop copies the files in GeoTiffDEM that are in DEMlist (within state boundary) to a new folder as 32 bit float, then into a geodatabase. 
for fn in DEMlist:
   
    infile = fn[:-1] + ".tif" 
   
    outfile = fn[:-1] + ".tif"
    
    outraster=out_workspace+"\\"+outfile
   
    # This copies all tiles in list as 32 bit float to a new folder
    outcopy = arcpy.CopyRaster_management(infile,outraster,pixel_type="32_bit_float",)
   
    # This copies all files created in Copy Raster to geodatabase, DEM_MN.gdb
    arcpy.RasterToGeodatabase_conversion(outcopy, "I:\GDBs\DEM_MN.gdb")

# Check in 3D Analyst and Spatial Analyst licenses
arcpy.CheckInExtension("3D")
arcpy.CheckInExtension("Spatial") 
