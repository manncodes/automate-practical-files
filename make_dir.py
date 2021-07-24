import os
import glob

# make given number of enumerated folders
def make_dir(num_folders, folder_name):
    for i in range(1, num_folders + 1):
        dir_name = folder_name + str(i)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)


make_dir(10, "practical ")
