# main.py

# modules
import os

# Set a working directory
work_dir = os.getcwd()

# Change to work directory
if os.getcwd() != work_dir:
    os.chdir(work_dir)

# folder management
folder_names = ["pyfunctions", "gui", "data_analysis"]

for folder in folder_names:
    if not os.path.exists(work_dir + "\\" + folder):
        os.mkdir(work_dir + "\\" + folder)
