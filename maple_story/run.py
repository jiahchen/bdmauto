# -*- coding: utf-8 -*-
from common.adb import ADB


if __name__ == "__main__":

    adb_object = ADB("127.0.0.1:5555")
    adb_object.connect()
    # adb_object.touch(("222", "284"))
    adb_object.capture()
    from maple_story.main_task import MainTask
    task = MainTask(adb_object)
    task.run()




# from pyadb.adb import adb_commands
# from pyadb.adb  import sign_m2crypto
# from pyadb.adb import ADB
# # device = adb_commands.AdbCommands()
# adb = ADB()
#
# adb.set_adb_path("./adb_exe/platform-tools/adb")
#
# print(adb.start_server())
# print(adb.connect_remote("locahost", 5555))
# print(adb.get_devices())
# adb.run_cmd("shell input tap 222284")
