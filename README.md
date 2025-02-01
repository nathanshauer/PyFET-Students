# PyFET (Python Finite Element Toolkit)
This project was created to help students develop their first finite element (FE) code for
elasticity problems applying object-oriented programming principles.

## Quick Steps

1. Change the folder name from `PyFET-Students` to `PyFET`.
2. Install all required libraries (see Required Libraries section).
3. Create an empty Python script at the same level as the `PyFET` directory (see Folder Structure section).
4. Fill the empty script with the following Python code:

```python
from PyFET.Node import *
n1 = Node([1,0])
print(f"node n1 = \n{n1}")
print("PyFET is working properly!")
```

If the message `PyFET is working properly!` appears, the installation is successful.

## Installing Python

To install Python, follow these steps:

1. Go to the official Python website: [python.org](https://www.python.org/).
2. Click on the "Downloads" tab.
3. Select the appropriate version for your operating system (Windows, macOS, or Linux).
4. Download the installer and run it.
5. Follow the installation instructions. Make sure to check the box that says "Add Python to PATH" during the installation process.

After installing Python, you can verify the installation by opening a terminal or command prompt and typing:

```sh
python --version
```

This should display the version of Python that you installed.

## Required Libraries

To use PyFET, you need to have the following libraries installed:

- **Python**: PyFET is written in Python, so you need Python installed on your system.
- **gmsh**: A 3D finite element grid generator required for mesh generation.
- **numpy**: A fundamental package for scientific computing with Python.
- **scipy**: A Python library used for scientific and technical computing.

You can install these libraries using pip:

```sh
python -m pip install gmsh numpy scipy
```

Make sure the Python version you are using is the same as the one you installed the libraries. It is no uncommon for an environment to have more than one Python version installed.

## Using PyFET as a Library

To use PyFET in your project, you need to import it into your Python script. Ensure that the PyFET directory is in the same directory as your script or in your Python path.

Here is an example of how to import and use PyFET:

```python
from PyFET.Bar2Node import *

# Your code to use PyFET
```

This will import all the functions related to the `Bar2Node` class that implements a 2-noded bar element.

## Folder Structure

Your folder structure should look something like this:

```
/your_project_directory
  /PyFET
    # All PyFET files
  your_script.py
```

## Generating Output in VTK Format

PyFET generates outputs in VTK format, which can be visualized using ParaView. Two functions should be implemented, one to simply visualize the domain and mesh, and another to visualize the solution fields after running. For the mesh/domain:

```python
# Printing mesh in vtk format
mesh.generateGeometryVTK("filename.vtk")
```

And to visualize the solution fields:

```python
vecnames = ["displacement"] # vector solution fields 
scalnames = ["normal", "strain", "stress"] # scalar solution fields
analysis.generateSolutionVTK(filename="filename.vtk",vecnames=vecnames,scalnames=scalnames)
```

## Visualizing with ParaView

To visualize the VTK output file, you can use ParaView:

1. Download ParaView from the official website: [paraview.org](https://www.paraview.org/download/).
2. Open ParaView.
3. Go to `File` > `Open` and select the `filename.vtk` file.
4. Click `Apply` to load the data.
5. Use the visualization tools in ParaView to explore your results.

With these steps, you should be able to set up and use PyFET for your finite element analysis projects.