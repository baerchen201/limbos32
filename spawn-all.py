from _thread import start_new_thread
from json import load
from os import system
from shutil import which
from time import sleep
from tkinter import messagebox
from typing import Any

import tk_msgbox_show

w1 = which("python")
w2 = which("python3")
cmd = "python" if (w2 == None or (w1 != None and ("WindowsApps" in w2))) else "python3"

counted = 0

try:
    with open("config.json") as f:
        data: dict[str, Any] = load(f)
        bsod = data.get("crash_on_failure", False)
    if bsod:
        response = str(
            tk_msgbox_show.show(
                "WARNING",
                "You have started this program with crash_on_failure enabled.\n"
                "This will crash your computer if you pick the wrong key.",
                messagebox.WARNING,
                messagebox.OKCANCEL,
            )
        )
        if response != messagebox.OK:
            tk_msgbox_show.show(
                "Cancelled",
                "The program will now terminate.\n"
                "You can disable crash_on_failure by modifying the config.json file",
            )
            exit(1)

except FileNotFoundError:
    pass


def threadeded():
    global counted
    system(cmd + " main.py")
    counted -= 1


for _ in range(8):
    counted += 1
    start_new_thread(threadeded, ())
    sleep(0.23)

while counted:
    sleep(0.1)
