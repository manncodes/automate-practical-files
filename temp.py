import os
import time
import logging
import subprocess
from tqdm import tqdm
from screenshot import getScreenshot

ROOT_DIR = os.path.dirname(__file__)
os.chdir(ROOT_DIR)
print(os.listdir("./practicals"))