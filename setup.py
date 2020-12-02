import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],
                     "includes": ['tkinter'],
                     "include_files": ['weather_icons', 'app_icon.png']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Weather",
      version="0.0.2",
      description="Weather in cities of the world",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", targetName='weather.exe', icon="sunny.ico", base=base)])

# pip install cx_freeze
# cd /f/ProjectPy/Weather_app
# python.exe setup.py build

