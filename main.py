import os
import subprocess
import time
from lib.adb import ADB, get_coordinates

"com.pearlabyss.blackdesertm.tw2/com.pearlabyss.blackdesertm.Loader"

dv1 = ADB("127.0.0.1:62001")
dv1.connect()
dv1.open_app("com.pearlabyss.blackdesertm.tw2", "com.pearlabyss.blackdesertm.Loader")
time.sleep(25)
dv1.capture()
dv1.touch(get_coordinates("google.png"))