import sys
import os
from cx_Freeze import setup, Executable
import tkinter

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter"]}

os.environ['TCL_LIBRARY'] = r'C:\Users\jqm2402\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\jqm2402\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(name='htmloutput',
version='0.1',
description='Convert peoplesoft bookmarks to google chrome',
options={"build_exe":build_exe_options},
executables=[Executable("htmloutput.py")])
