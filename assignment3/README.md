#Zale Heller TechDirecting assignment 3

This is a Python script for creating three kinds of basic geo (cubes, spheres, and cylinders) with materials in Maya using batch mode. You can also customize the color of the materials and save them in Maya ASCII files. 

REQUIREMENTS:
- Use Autodesk Maya 2020 or later
- Python 3.7 or later for this specific script 
- Enable mayapy!

TO INSTALL: 
- Save the script as `lesson3.py`
- Ensure the script has executable permissions (Unix/Linux/Mac):

The script should include error handling for:
- Invalid geo types
- File permission issues
- Maya initialization errors
- Invalid color values

If an error occurs, the script will:
1. Print an error message to stderr
2. Exit with status code 1
3. Properly clean up Maya standalone initialization

