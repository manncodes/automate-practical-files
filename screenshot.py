import os
import time
import logging
import pyautogui
import pygetwindow
from PIL import Image

#for logging progress
logging.basicConfig(filename="practicalfiles.log",filemode='w+', level=logging.INFO)

def getScreenshot(working_directory, img_filename, debug=False):
    titles = pygetwindow.getAllTitles()
    if debug:
        print(titles)

    pyruntime_title_contains = ["cmd.exe", ".py"]

    normal_runtime_title_contains = [
        "cmd.exe",
    ]

    def get_title_name(titles, title_prefix):
        for title in titles:
            if all(title.find(pref) != -1 for pref in title_prefix):
                return title

    # wait until the python script is running
    while True:
        titles = pygetwindow.getAllTitles()
        title = get_title_name(titles, pyruntime_title_contains)
        if title == None:
            break
        else:
            logging.warning(f"script still running @  {title}")
            time.sleep(3)

    titles = pygetwindow.getAllTitles()
    cmd_title = get_title_name(titles, normal_runtime_title_contains)

    if debug:
        logging.info(">>>", cmd_title)
    cmd = pygetwindow.getWindowsWithTitle(cmd_title)[0]
    cmd.activate()

    x1, y1 = cmd.topleft
    width, height = cmd.size
    x2 = x1 + width
    y2 = y1 + height

    save_img_path = os.path.join(working_directory, img_filename + "_cmd.png")
    pyautogui.screenshot(save_img_path)

    im = Image.open(save_img_path)
    im = im.crop((x1, y1, x2, y2))
    im.save(save_img_path)
    logging.info(f"image saved to {save_img_path}")

    cmd.close()
