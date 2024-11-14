#Zale Heller TechDirecting assignment 3

This is a Python script for creating three kinds of basic geo (cubes, spheres, and cylinders) with materials in Maya using batch mode. You can also customize the color of the materials and save them in Maya ASCII files. 

- Use Autodesk Maya 2020 or later
- Python 3.7 or later for this specific script 
- Enable mayapy!

TO INSTALL: 
- Save the script as `maya_geometry_creator.py`
- Ensure the script has executable permissions (Unix/Linux/Mac):
```bash

#Basic Command Structure
```bash
mayapy maya_geometry_creator.py --type GEOMETRY_TYPE --color R G B --output OUTPUT_PATH
```

#Arguments
- `--type` or `-t`: Type of geometry to create (required)
  - Choices: `cube`, `sphere`, `cylinder`
- `--color` or `-c`: RGB color values between 0-1 (optional)
  - Default: `1 1 1` (white)
  - Format: Three float values for R G B
- `--output` or `-o`: Output path for Maya ASCII file (required)
  - Must end with `.ma`

#Examples

Create a white cube:
```bash
mayapy maya_geometry_creator.py --type cube --output cube.ma
```

Create a red sphere:
```bash
mayapy maya_geometry_creator.py --type sphere --color 1 0 0 --output red_sphere.ma
```

Create a blue cylinder:
```bash
mayapy maya_geometry_creator.py --type cylinder --color 0 0 1 --output blue_cylinder.ma
```

### Linux
```bash
/usr/autodesk/maya2023/bin/mayapy maya_geometry_creator.py --type cube --output /path/to/output/cube.ma
```

#Error Handling
The script includes error handling for:
- Invalid geo types
- File permission issues
- Maya initialization errors
- Invalid color values

If an error occurs, the script will:
1. Print an error message to stderr
2. Exit with status code 1
3. Properly clean up Maya standalone initialization

THis script outputs:
1. A Maya ASCII file (.ma) containing:
   - The specified geometry
   - A Lambert material with the specified color
   - Proper shading group assignments

This script uses:
- `maya.standalone` for batch operations
- `maya.cmds` for Maya commands
- `argparse` for command line argument parsing
- Lambert shaders for materials
