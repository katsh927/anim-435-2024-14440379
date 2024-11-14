#Zale Heller TechDirecting Lesson 3 

import argparse  
import maya.standalone  #THIS is batch mode
import maya.cmds as cmds  
import sys  #for system operations like exit codes

def initialize_maya():
    """Initialize Maya in batch mode"""
    #""" = 'big comment' 
    #start maya in standalone mode 
    maya.standalone.initialize()
    #so you can load required plugins (which ones would be relevant to this assignment, verify)
    #cmds.loadPlugin("matrixNodes", quiet=True)

def create_geometry(geo_type, color):
    """Create geometry and assign material
    
    Args:
        geo_type (str): Type of geometry ('cube', 'sphere', or 'cylinder')
        color (list): RGB color values as floats [r, g, b]
    
    Returns:
        str: Name of created geometry
    """
    #initialize geo  variable
    geo = None
    #make geo type lowercase-- case sensitive 
    geo_type = geo_type.lower()
    
    #create the specified geometry type
    if geo_type == 'cube':
        geo = cmds.polyCube()[0]  # [0] gets the geometry name from the returned tuple
    elif geo_type == 'sphere':
        geo = cmds.polySphere()[0]
    elif geo_type == 'cylinder':
        geo = cmds.polyCylinder()[0]
    else:
        raise ValueError(f"Invalid geometry type: {geo_type}")
    
    #creates lambert NODE 
    material = cmds.shadingNode("lambert", asShader=True)
    #assigns color
    cmds.setAttr(f"{material}.color", color[0], color[1], color[2], type="double3")
    
    #make shading group 
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
    #connects your material to shading group
    cmds.connectAttr(f"{material}.outColor", f"{shading_group}.surfaceShader")
    #assign the shading group to the geo
    cmds.sets(geo, edit=True, forceElement=shading_group)
    
    return geo

def save_scene(output_path):
    """Save the Maya scene
    
    Args:
        output_path (str): Path to save the Maya file
    """
    #rename current scene to output path
    cmds.file(rename=output_path)
    #set file type 
    cmds.file(save=True, type='mayaAscii')

def main():
    #set up argparse 
    parser = argparse.ArgumentParser(description='Create geometry with material in Maya batch mode')
    
    #arg for geo type
    parser.add_argument('--type', '-t',
                      required=True,
                      choices=['cube', 'sphere', 'cylinder'],
                      help='Type of geometry to create')
    
    #arg for color values
    parser.add_argument('--color', '-c',
                      nargs=3,  # Expects 3 values for RGB
                      type=float,  # Values should be floats
                      default=[1.0, 1.0, 1.0],  # Default to white
                      metavar=('R', 'G', 'B'),
                      help='RGB color values (0-1). Default: 1 1 1 (white)')
    
    #arg for output file path
    parser.add_argument('--output', '-o',
                      required=True,
                      help='Output path for Maya file (.ma)')

    #parse the command line arguments
    args = parser.parse_args()

    try:
        #start maya in batch mode
        initialize_maya()
        #new scene
        cmds.file(new=True, force=True)
        #create geo and assign material
        geo = create_geometry(args.type, args.color)
        print(f"Created {args.type} with name: {geo}")
        
        #save scene to specified location
        save_scene(args.output)
        print(f"Saved scene to: {args.output}")
        
    except Exception as e:
        #theoretically handles issues during executio 
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)  # Exit with error code
    finally:
        #clean up Maya standalone
        maya.standalone.uninitialize()

#entry point of the code 
if __name__ == '__main__':
    main()