# -*- coding: utf-8 -*-
import time
COORDINATES = {
    "menu": [("1820", "25"), ("1887", "73")],
    "challenge": [("510", "11"), ("594", "103")],
    "mail": [("1320", "11"), ("1430", "103")],
    "task": [("310", "173"), ("403", "276")],
    "task_detail": [("368", "144"), ("1196", "294")],
    "auto_task": [("1560", "903"), ("1848", "1000")],
    "auto_attack": [("", ""), ("", "")],
    "skip": [("90", "62"), ("203", "97")],
    "accept": [("1528", "887"), ("1888", "965")],
    "accept_gift": [("758", "878"), ("1163", "975")],
    "finish": [("1528", "887"), ("1888", "965")]
}
print(*COORDINATES.get("menu"))

class MainTask(object):
    def __init__(self, adb):
        self.adb = adb
        pass
    def accept_task(self):
        self.adb.touch(COORDINATES.get("menu"))
        self.adb.touch(COORDINATES.get("challenge"))
        self.adb.touch(COORDINATES.get("task"))
        self.adb.touch(COORDINATES.get("task_detail"))
        self.adb.touch(COORDINATES.get("auto_task"))

        # check skip
        while self.adb.check_status(COORDINATES, "skip") != 1:
            time.sleep(2)
        self.adb.touch(COORDINATES.get("skip"))
        self.adb.touch(COORDINATES.get("accept"))

        while self.adb.check_status(COORDINATES, "skip") != 1:
            time.sleep(2)
        self.adb.touch(COORDINATES.get("skip"))
        self.adb.touch(COORDINATES.get("finish"))
        self.adb.touch(COORDINATES.get("accept_gift"))

    def run(self):
        self.accept_task()
