# LaserSaver
Main LaserSaver Code
The purpose of this project is to help find the holes in a piece of material that has been cut by a lasercutter.
This will include all instructions for building the physical scanner as well as installing the software.

# Install Instructions
This will only run on python 2.7.x

These are the instructions for installing the dependencies for the project.
### Install Instructions for Debian
Use our script to install all dependencies and link code. By running the following commands from the terminal
```
$ sudo install_opencv.sh
$ python setup.py install
```

### Install Instructions for Windows
We recommend you install anaconda as your python distribution

Install opencv 3.0.0 by following the instructions from prebuilt binaries at this link

http://docs.opencv.org/3.1.0/d5/de5/tutorial_py_setup_in_windows.html#gsc.tab=0

Then run the following commands from the command prompt
```
pip install setuptools
python setup.py install
```

### Install Instructions for OSX
We recommend you install anaconda as your python distribution

Install opencv 3.0.0

http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/

Then run the following commands from the terminal
```
pip install setuptools
python setup.py install
```

## Hardware Shopping List
The parts needed to construct the scanner.

[Click Here for the Shopping List] (Shopping_List.md)

## Assembly Instructions
How to assemble the scanner.

[Click Here for the Assembly Instructions] (Assembly_instructions.md)
