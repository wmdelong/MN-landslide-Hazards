# MN-landslide-Hazards
This repo contains code used to process various raster data products as part of an LCCMR-funded project studying landslides throughout the state of Minnesota with a goal of mitigating landslide hazard risk

Workflow below:

-Tile.txt 
This script tiles the 1 m resolution DEM of Minnesota into 2 km x 2 km tiles with 50 m overlap for subsequent processing.

-DEM_to_ALLGDB.py
This script moves all tiles with data to a master ESRI geodatabase (necessary because of huge number of NoData tiles created in 	previous step). 

-DEM_to_AOIGDB.py
This script pulls DEM tiles from the geodatabase containing all DEM tiles and writes relevant tiles to area of interest (AOI) 		geodatabases.

-DEM_Processing.py 
This script uses the arcpy module to create the five products (Hillshade with 45* and 315* azimuth, aspect, slope, standard, planform, profile curvatures) for each AOI. 

-Open_to_AOIGDB.py
This script moves topographic openness rasters from GDB containing all tiles to AOI GDBs.

-Resample.py
This script resamples a raster; in this case used to resample from 1m x 0.9999 m to 1 m x 1 m. 

CopyRaster_32.py
This script copies a given raster to 32 bit float data type. 

Openness_modelbuilder.py
This script is the automated python output of ArcGIS model to calculate topographic openness using SAGA GIS module.

-GIS_Data_UserGuide.pdf
	This workflow was created and distributed to other members of the project as a guide for downloading, preparing, and using all 
	data created. There is a wide range of GIS expertise on this project, so this document is geared toward those who lack experience 	  with ArcGIS. 
