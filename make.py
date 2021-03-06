import os
import time
import logging
import subprocess
from tqdm import tqdm
from screenshot import getScreenshot

PRACTICAL_DIR_NAME = "practicals"

PRACTICAL_DIR = os.path.join(os.getcwd(), PRACTICAL_DIR_NAME) 

os.chdir(PRACTICAL_DIR)

logging.basicConfig(filename="practicalfiles.log", level=logging.INFO)

# IF YOU WANT AUTOMATED FILE DIRECTORY STRUCTURE RUN 'make_dir.py'

#ENTER YOUR RECURRING PRACTICAL FOLDER NAME PREFIX HERE:
# e.g for directories like ['practical_1', 'practical_2', 'practical_3'], -> PRACTICAL_PREFIX = 'practical_'
# e.g for directories like ['practical 1', 'practical 2', 'practical 3']-> PRACTICAL_PREFIX = 'practical'
# e.g for directories like ['p1', 'p2', 'p3'] -> PRACTICAL_PREFIX = 'p' BUT THIS ONE IS NOT ADVISIBLE. THINK WHY!
PRACTICAL_PREFIX = "practical" 

# get folder names in a directory
practical_dirs = [
    name
    for name in os.listdir(".")
    if (os.path.isdir(name) and name.find(PRACTICAL_PREFIX) != -1)
]

# function to get file names in a directory
def get_file_names(dir_name):
    return [
        name
        for name in os.listdir(dir_name)
        if (os.path.isfile(os.path.join(dir_name, name)) and name.find(".py") != -1)
    ]


practical_dirs = sorted(practical_dirs, key=len)
print(practical_dirs)

for practical_dir_name in tqdm(practical_dirs, desc="overall progress", position=0):
    files = get_file_names(practical_dir_name)
    os.chdir(practical_dir_name) # change to practical's directory

    for file in tqdm(files, desc=f"{practical_dir_name} progress", position=1, leave=False):
        # do shit here
        pyprocess = subprocess.check_call(
            ["start", "cmd", "/wait", "/k", "python", file],
            stdout=subprocess.PIPE,
            shell=True,
        )
        time.sleep(1)  # for letting subprocess atleast spawn
        getScreenshot(
            working_directory=os.path.join(PRACTICAL_DIR, practical_dir_name),
            img_filename=file.split(".")[0],
        )
        
    os.chdir(PRACTICAL_DIR) # go back to main directory
    logging.info(f"All screenshots of {practical_dir_name} are done.")


print("Finished screenshotting all the files!")
print("Check log files for more info if error persist!")
