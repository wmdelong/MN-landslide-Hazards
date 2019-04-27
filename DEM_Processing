# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:12:50 2018

@author: Whitney DeLong
"""

import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True

arcpy.CheckOutExtension("Spatial")

env.workspace = r"I:\2012_DEM_tiles"
#out_workspace1 = r"I:\GDBs\Northeast\Hillshade_45.gdb" 
#out_workspace2 = r"I:\GDBs\Northeast\Hillshade_315.gdb"
out_workspace3 = r"I:\2012_slope_tiles"
#out_workspace4 = r"I:\GDBs\Northeast\Curvature_Standard.gdb"
#out_workspace5 = r"I:\GDBs\Northeast\Curvature_Planform.gdb"
#out_workspace6 = r"I:\GDBs\Northeast\Curvature_Profile.gdb"
#out_workspace7 = r"I:\GDBs\Northeast\Aspect.gdb"

##hillshade 45 degree azimuth
#for dem in arcpy.ListRasters("*_dem"): 
#    if dem > "MN_147_165_dem":
#        outshd = arcpy.Describe(dem).baseName + "_shd45"  
#        outraster = out_workspace1 + "\\" + outshd
#    
##        # Set local variables
#        inRaster = dem
#        azimuth = 45
#        altitude = 45
#        modelShadows = "NO_SHADOWS"
#        zFactor = 1
#
#    # Execute HillShade
#        outHillShade = Hillshade(inRaster, azimuth, altitude, modelShadows, zFactor)
#
#    # Save the output 
#        outHillShade.save(outraster)
#
#
##hillshade 315 degree azimuth 
#for dem in arcpy.ListRasters("*_dem"):
#    outshd2 = arcpy.Describe(dem).baseName + "_shd315"
#    outraster2 = out_workspace2 + "\\" + outshd2
#    
#    # Set local variables
#    inRaster = dem
#    azimuth = 315
#    altitude = 45
#    modelShadows = "NO_SHADOWS"
#    zFactor = 1
#
#    # Execute HillShade
#    outHillShade = Hillshade(inRaster, azimuth, altitude, modelShadows, zFactor)
#
#    # Save the output 
#    outHillShade.save(outraster2)

#Slope map in degrees
for dem in arcpy.ListRasters("*.tif"):
    outslp = arcpy.Describe(dem).baseName + "_slp.tif"
    outraster3 = out_workspace3 + "\\" + outslp
   
    
    # Set local variables
    inRaster = dem
    outMeasurement = "DEGREE"
    zFactor = 1

    # Execute Slope
    outSlope = Slope(inRaster, outMeasurement, zFactor)

    # Save the output 
    outSlope.save(outraster3) 

##Three curvature maps: standard, planform, and profile (not sure if we need these) 
#for dem in arcpy.ListRasters("*_dem"):
#    outCurv = arcpy.Describe(dem).baseName + "_curv"      
#    outraster4 = out_workspace4 + "\\" + outCurv
#    outPlanCurv = arcpy.Describe(dem).baseName + "_plancurv"   
#    outraster5 = out_workspace5 + "\\" + outPlanCurv
#    outProfCurv = arcpy.Describe(dem).baseName + "_profcurv"   
#    outraster6 = out_workspace6 + "\\" + outProfCurv
#    
#    # Set local variables
#    inRaster = dem
#    zFactor = 1
#
#    #Execute Curvature
#    outCurve = Curvature(inRaster, 1, outraster5, outraster6)
#
#    # Save the output 
#    outCurve.save(outraster4)
#
#
##Aspect
#for dem in arcpy.ListRasters("*_dem"):
#    outasp = arcpy.Describe(dem).BaseName + "_Asp"
#    outraster7 = out_workspace7 + "\\" + outasp
#    
#    #Set local variables
#    inRaster = dem
#    
#    #Execute Aspect
#    outAspect = Aspect(inRaster)
#    
#    #Save the output
#    outAspect.save(outraster7)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
