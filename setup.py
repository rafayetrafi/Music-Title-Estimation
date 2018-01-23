import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

include_files = ["autorun.inf"]
base = None

if sys.platform == "win32":
    base = "win32GUI"

setup(name = "Music Title Estimator",
      version = "0.1",
      description = "Developed By Rafayet Hossain. E-mail: rafayet3994@diu.edu.bd",
      options = {'build.exe': {'include_files':include_files}},
      executables = [Executable("titleestimator.py",base=base)])

