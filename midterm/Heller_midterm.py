#Zale Heller ANIM435 Midterm 

import csv

import maya.cmds as cmds 

import maya.standalone

import argparse
import os
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load and set up cameras from CSV in Maya.")
    parser.add_argument('--camera_csv', type=str, help="Path to CSV with camera data", required=True)
    return parser.parse_args()

def load_cameras_from_csv(csv_path):
    cameras = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cameras.append(row)
    return cameras

def create_camera(name, filmback_width, filmback_height, focal_length, chart_path):
    cam_shape = cmds.camera(name=name)[1]
    cmds.setAttr(f"{cam_shape}.horizontalFilmAperture", filmback_width)
    cmds.setAttr(f"{cam_shape}.verticalFilmAperture", filmback_height)
    cmds.setAttr(f"{cam_shape}.focalLength", focal_length)
    
    #create image plane for framing chart... hopefully 
    if chart_path:
        img_plane = cmds.imagePlane(fileName=chart_path, showInAllViews=False)
        cmds.parent(img_plane[0], cam_shape, shape=True)
    
    return cam_shape

def create_camera_ui(cameras):
    window = cmds.window(title="Camera Loader", widthHeight=(400, 200))
    cmds.columnLayout(adjustableColumn=True)
    
    cmds.text(label="Select Camera:")
    
    camera_list = [] 
    for cam in cameras:
        camera_list.append(cam['camera']) 
        #print(cam)

    
    cmds.optionMenu("camera_menu", changeCommand=lambda cam_name: on_camera_selected(cam_name, cameras))
    for cam_name in camera_list:
        cmds.menuItem(label=cam_name)
    
    cmds.showWindow(window)

def on_camera_selected(cam_name, cameras):
    camera_data = next(cam for cam in cameras if cam['camera'] == cam_name)
    create_camera(camera_data['camera'], float(camera_data['horizontal_aperture']), float(camera_data['vertical_aperture']), 
                  float(camera_data['focal_length']), 5) #camera_data['chart_path'])
                  
             

def main():
  #  maya.standalone.initialize(name='python')
    #args = parse_arguments()
    #print(args.camera_csv)
    #cameras = load_cameras_from_csv(args.camera_csv)
    cameras = load_cameras_from_csv("cameras.csv")
    create_camera_ui(cameras)

if __name__ == "__main__":
    #main()
    #print(os.listdir())
    path = os.path.realpath("__file__")
    print("PLEASE WORK JFC")
    print(Path.cwd())
    print(path)
    cameras = load_cameras_from_csv("C:/Users/fedor/Videos/cameras.csv")
    print(cameras)
    create_camera_ui(cameras)
  
    