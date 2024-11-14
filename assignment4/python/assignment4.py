#Zale Heller TechDirecting Lesson 4 

#!/usr/bin/env python

import maya.cmds as cmds
import os
import sys

def create_named_geometry():
    """
    Creates a cube with name from environment variable MAYA_GEO_NAME
    Returns:
        str: Name of created geometry or None if environment variable is not found
    """
    try:
        #get geo name from environment variable
        geo_name = os.getenv('MAYA_GEO_NAME')
        
        if not geo_name:
            print("Error: Environment variable MAYA_GEO_NAME not set")
            return None
            
        # Create cube with specified name
        cube = cmds.polyCube(name=geo_name)[0]
        
        # Print confirmation
        print(f"Created cube named: {cube}")
        print(f"Environment variable MAYA_GEO_NAME value: {geo_name}")
        
        return cube
        
    except Exception as e:
        print(f"Error creating geometry: {str(e)}")
        return None

#RUN THIS IF NOT IN STANDALONE 
if __name__ == '__main__':
    if not cmds.about(batch=True):
        create_named_geometry() 