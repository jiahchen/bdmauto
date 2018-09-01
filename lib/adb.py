
import subprocess
import os
ADB_PATH = os.path.join(os.path.join(os.path.dirname((os.path.dirname(__file__))), "adb"), "adb.exe")
IMG_PATH = os.path.join(os.path.dirname((os.path.dirname(__file__))), "img")
# IMG_PATH = os.path.join(os.path.join(os.path.dirname((os.path.dirname(__file__))), "img"), "screenshot.png")
# IMG_PATH = os.path.join(os.path.dirname((os.path.dirname(__file__))), "screenshot.png")

class ADB():
    def __init__(self, device):
        self.device = device

    def connect(self):
        subprocess.call([ADB_PATH, "connect", self.device])

    def open_app(self, pack_name, activity_name):
        openapp_command = self.command
        openapp_command.extend(["shell", "am", "start", "%s/%s" % (pack_name, activity_name)])
        subprocess.call(openapp_command)

    def touch(self, coordinate):
        touch_command = self.command
        touch_command.extend(["shell", "input", "tap"])
        touch_command.extend(list(coordinate))
        subprocess.call(touch_command)

    @property
    def command(self):
        return [ADB_PATH, "-s", self.device]

    def capture(self, phone_path="/sdcard/screen.png"):

        capture_command = self.command
        capture_command.extend(["shell", "screencap", "-p", phone_path])
        subprocess.call(capture_command)
        
        pull_command = self.command
        pull_command.extend(["pull", phone_path, os.path.join(IMG_PATH, "screenshot.png")])
        subprocess.call(pull_command)
    
# class Parser():
#     def __init__(self): 



import cv2
def get_coordinates(target_nm, find_screen_nm="screenshot.png"):
    target = cv2.imread(os.path.join(IMG_PATH, target_nm))
    find_screen = cv2.imread(os.path.join(IMG_PATH, find_screen_nm))

    result = cv2.matchTemplate(target, find_screen, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) 

    find_height, find_width, find_channel = target.shape[::]
    
    x = str(int(max_loc[0] + (find_width / 2)))
    y = str(int(max_loc[1] + (find_height / 2)))
    return x, y

