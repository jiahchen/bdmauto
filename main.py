import os
import subprocess
import time
from lib.adb import ADB, get_coordinates

# dv1 = ADB("127.0.0.1:62001")
# dv1.connect()
# dv1.open_app("com.pearlabyss.blackdesertm.tw2", "com.pearlabyss.blackdesertm.Loader")
# time.sleep(25)
# dv1.capture()
# dv1.touch(get_coordinates("google.png"))

# while True:
#     dv1.capture()
#     time.sleep(5)


class BlackM(object):
    def __init__(self, device):
        self.adb = ADB(device)
        
        self.adb.keep_screen_shot()
    
    def touch_task(self):
        self.adb.touch(["1230", "170"])
        time.sleep(0.5)
        self.adb.touch(["1230", "170"])

    def auto_main_task(self):
        while True:
            self.touch_task()
            
            # check finish
            while self.adb.check_status(self.sample_img, "task_complete") != 1:
                time.sleep(2)
            self.touch_task()
            # conversavtion
            # check task done
        #     self.adb.check_status(self.sample_img, "task_complete")
        # print(self.sample_img)
        # print()
    @property
    def sample_img(self):
        imgs = {"task_complete": [(985, 175), (1014, 186)]}
        return imgs
    

game1 = BlackM("127.0.0.1:62001")
# game1.touch_task()
time.sleep(1)
game1.auto_main_task()
