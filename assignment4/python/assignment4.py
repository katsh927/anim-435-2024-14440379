#Zale Heller TechDirecting Lesson 4 
import os
import maya.cmds as cmds

def create_geometry_from_env():
    
    #geo name from environment variable
    geometry_name = os.environ.get('ASSET')
    
    if not geometry_name:
        raise ValueError("Environment variable 'ASSET' is not set. Please set it before running this script.")
    
    try:
        #create a sphere 
        sphere = cmds.polySphere(name=f"{geometry_name}_sphere", radius=2)[0]
        
        #create a cube
        cube = cmds.polyCube(name=f"{geometry_name}_cube", width=3, height=3, depth=3)[0]
        
        #move the cube above the sphere 
        cmds.move(0, 4, 0, cube)
        
        #group the geo 
        group_name = f"{geometry_name}_group"
        cmds.group(sphere, cube, name=group_name)
        
        print(f"Successfully created geometry with base name: {geometry_name}")
        print(f"Created objects: {sphere}, {cube}")
        print(f"Grouped under: {group_name}")
        
    except Exception as e:
        cmds.warning(f"Error creating geometry: {str(e)}")
        raise

if __name__ == "__main__":
    create_geometry_from_env()