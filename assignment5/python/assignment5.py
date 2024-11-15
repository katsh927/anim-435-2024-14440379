#Zale Heller TechDirecting assignment 5 

import csv
import maya.cmds as cmds
import maya.standalone
import argparse
import os
import logging
from pathlib import Path

#configure logging
logger = logging.getLogger('MayaCameraLoader')
logger.setLevel(logging.DEBUG)

#console handler with a custom formatter
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(funcName)s: %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load and set up cameras from CSV in Maya.")
    parser.add_argument('--camera_csv', type=str, help="Path to CSV with camera data", required=True)
    return parser.parse_args()

def load_cameras_from_csv(csv_path):
    cameras = []
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cameras.append(row)
        logger.info(f"Successfully loaded {len(cameras)} cameras from {csv_path}")
        return cameras
    except FileNotFoundError:
        logger.error(f"CSV file not found at path: {csv_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading CSV file: {str(e)}")
        raise

def create_camera(name, filmback_width, filmback_height, focal_length, chart_path):
    logger.warning(f"Preparing to generate new camera: {name}")
    cam_shape = cmds.camera(name=name)[1]
    cmds.setAttr(f"{cam_shape}.horizontalFilmAperture", filmback_width)
    cmds.setAttr(f"{cam_shape}.verticalFilmAperture", filmback_height)
    cmds.setAttr(f"{cam_shape}.focalLength", focal_length)
    
    #framing chart 
    if chart_path:
        logger.info(f"Adding image plane from chart: {chart_path}")
        img_plane = cmds.imagePlane(fileName=chart_path, showInAllViews=False)
        cmds.parent(img_plane[0], cam_shape, shape=True)
    else:
        logger.debug("No chart path provided, skipping image plane creation")
    
    logger.info(f"Successfully created camera: {name}")
    return cam_shape

def create_camera_ui(cameras):
    logger.debug("Initializing camera UI")
    window = cmds.window(title="Camera Loader", widthHeight=(400, 200))
    cmds.columnLayout(adjustableColumn=True)
    
    cmds.text(label="Welcome to Your Camera Bag. Please select a camera based on your desired specs:")
    camera_list = []
    for cam in cameras:
        camera_list.append(cam['camera'])
    
    cmds.optionMenu("camera_menu", changeCommand=lambda cam_name: on_camera_selected(cam_name, cameras))
    for cam_name in camera_list:
        cmds.menuItem(label=cam_name)
    
    cmds.showWindow(window)
    logger.info("Camera UI created successfully!")

def on_camera_selected(cam_name, cameras):
    logger.debug(f"Camera selected: {cam_name}")
    camera_data = next(cam for cam in cameras if cam['camera'] == cam_name)
    create_camera(
        camera_data['camera'],
        float(camera_data['horizontal_aperture']),
        float(camera_data['vertical_aperture']),
        float(camera_data['focal_length']),
        5 #camera_data['chart_path']
    )

def main():
    logger.info("Starting camera loader application...")
    cameras = load_cameras_from_csv("cameras.csv")
    create_camera_ui(cameras)

if __name__ == "__main__":
    path = os.path.realpath("file")
    print("One moment, loading...")
    print(Path.cwd())
    print(path)
    try:
        logger.info("Attempting to load cameras from CSV, please wait a few seconds.")
        cameras = load_cameras_from_csv("C:/Users/fedor/Videos/cameras.csv")
        print(cameras)
        create_camera_ui(cameras)
    except Exception as e:
        logger.error(f"Failed to initialize camera loader. Please check that your csv is correctly connected and try again.")

        #I'm admittedly not sure if I did this right because I couldn't get my desired error messages to show. 