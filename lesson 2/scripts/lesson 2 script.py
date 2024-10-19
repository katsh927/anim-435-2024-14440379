import maya.cmds as cmds

def create_geometry_with_material():
    #new window 
    window = cmds.window(title="Create Geometry and Assign Material", widthHeight=(300, 150))
    cmds.columnLayout(adjustableColumn=True)
    
    #select geo type
    cmds.text(label="Choose Geometry Type:")
    cmds.radioButtonGrp("geoType", labelArray3=["Cube", "Sphere", "Cylinder"], numberOfRadioButtons=3, select=1)
    
    #select material 
    cmds.text(label="Select Material Color:")
    cmds.colorSliderGrp("color", label="Color")
    
    #create button 
    cmds.button(label="Create", command=create_geometry)
    
    #make window visible
    cmds.showWindow(window)

def create_geometry(*args):
    #get selected geo type
    geo_type = cmds.radioButtonGrp("geoType", query=True, select=True)
    geo = None
    
    if geo_type == 1:  #CUBE
        geo = cmds.polyCube()[0]
    elif geo_type == 2:  #SPHERE
        geo = cmds.polySphere()[0]
    elif geo_type == 3:  #CYLINDER
        geo = cmds.polyCylinder()[0]
    
    #select color
    color = cmds.colorSliderGrp("color", query=True, rgb=True)
    
    #create material and assign to geo
    material = cmds.shadingNode("lambert", asShader=True)
    cmds.setAttr(material + ".color", color[0], color[1], color[2], type="double3")
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
    cmds.connectAttr(material + ".outColor", shading_group + ".surfaceShader")
    cmds.sets(geo, edit=True, forceElement=shading_group)

create_geometry_with_material()
