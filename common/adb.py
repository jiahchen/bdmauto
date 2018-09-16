
import subprocess
import os
import time
from threading import Thread
import imagehash
from common.const import ADB_PATH, IMG_PATH
import cv2


class ADB(object):
    def __init__(self, device):
        self.device = device
        self.screenshot_flag = False

    def connect(self):
        subprocess.call([ADB_PATH, "connect", self.device])

    def open_app(self, pack_name, activity_name):
        openapp_command = self.command
        openapp_command.extend(["shell", "am", "start", "%s/%s" % (pack_name, activity_name)])
        subprocess.call(openapp_command)

    def touch(self, coordinate):
        touch_command = self.command
        touch_command.extend(["shell", "input", "tap"])
        if len(coordinate) == 1:
            touch_command.extend(list(coordinate))
            print(touch_command)
        elif len(coordinate) == 2:
            x = str((int(coordinate[0][0])+int(coordinate[1][0]))/2)
            y = str((int(coordinate[0][1]) + int(coordinate[1][1])) / 2)
            touch_command.extend([x, y])
        subprocess.call(touch_command)
        time.sleep(2)

    @property
    def command(self):
        return [ADB_PATH, "-s", self.device]

    def capture(self, phone_path="/sdcard/screen.png"):

        capture_command = self.command
        capture_command.extend(["shell", "screencap", "-p", phone_path])
        subprocess.call(capture_command)

        pull_command = self.command
        pull_command.extend(["pull", phone_path, os.path.join(IMG_PATH, "screenshot.png")])
        self.screenshot_flag = True
        subprocess.call(pull_command)
        self.screenshot_flag = False

    def keep_screen_shot(self):
        th = Thread(target=self.keep_screen_shot_fn)
        th.start()

    def keep_screen_shot_fn(self):
        while True:
            self.capture()
            time.sleep(1)
    
    def crop(self, target_img, loc, find_screen_nm="screenshot.png"):
        (x, y), (x1, y1) = loc

        # lock and wait
        while self.screenshot_flag:
            time.sleep(0.1)
        self.capture()

        screen_shot = cv2.imread(os.path.join(IMG_PATH, find_screen_nm))[int(y):int(y1), int(x):int(x1)]
        cv2.imwrite(os.path.join(IMG_PATH, 'tmp_%s.png' % target_img), screen_shot)
        time.sleep(0.1)
        return screen_shot

    def check_status(self, sample_img, target_img):
        from PIL import Image

        target_hash = imagehash.phash(Image.open(os.path.join(IMG_PATH, '%s.png' % target_img)))
        self.crop(target_img, sample_img[target_img])

        screen_shot_hash = imagehash.phash(Image.open(os.path.join(IMG_PATH, 'tmp_%s.png' % target_img)))
        point = target_hash - screen_shot_hash
        print(point)
        return 1 if point <= 10 else 0


# def get_coordinates(target_nm, find_screen_nm="screenshot.png"):
#     target = cv2.imread(os.path.join(IMG_PATH, target_nm))
#     find_screen = cv2.imread(os.path.join(IMG_PATH, find_screen_nm))
#
#     result = cv2.matchTemplate(target, find_screen, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
#     find_height, find_width, find_channel = target.shape[::]
#
#     x = str(int(max_loc[0] + (find_width / 2)))
#     y = str(int(max_loc[1] + (find_height / 2)))
#     return x, y

