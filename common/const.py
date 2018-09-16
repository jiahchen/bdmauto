# -*- coding: utf-8 -*-
import os
import platform
PROJECT_PATH = os.path.dirname((os.path.dirname(__file__)))
PLATFORM = platform.system()

if PLATFORM == "Darwin":
    ADB_PATH = os.path.join(PROJECT_PATH, os.path.join("adb_exe", os.path.join("platform-tools", "adb")))
elif PLATFORM == "Window":
    ADB_PATH = os.path.join(PROJECT_PATH, os.path.join("adb_exe", "adb.exe"))

IMG_PATH = os.path.join(PROJECT_PATH, "img")
