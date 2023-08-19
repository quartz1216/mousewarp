import win32gui
import win32api
import win32con
import pystray
import time
import threading
from PIL import Image
import sys
from pathlib import Path
from plyer import notification

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', str(Path(__file__).absolute().parent))
    return str(Path(base_path).joinpath(relative_path))

def on_exit(icon,item):
    icon.stop()

def get_active():
    active = win32gui.GetForegroundWindow()
    return active

def move_mouse(hwnd):
    try:
        rect = win32gui.GetWindowRect(hwnd)
        x = (rect[0] + rect[2]) // 2
        y = (rect[1] + rect[3]) // 2
        win32api.SetCursorPos((x,y))
    except win32gui.error:
        pass

def move_cursor_thread():
    active_hwnd = None
    while True:
        time.sleep(0.1)
        if win32api.GetAsyncKeyState(win32con.VK_MENU) & 0x8000:
            while win32api.GetAsyncKeyState(win32con.VK_MENU) & 0x8000:
                time.sleep(0.1)
            hwnd = get_active()
            if active_hwnd != hwnd: 
                move_mouse(hwnd)
                active_hwnd = get_active()

image = Image.open(resource_path("icon.ico"))
menu = (pystray.MenuItem("Exit", on_exit),) 
icon = pystray.Icon("name", image, "MouseWarp", menu)

cursor_thread = threading.Thread(target = move_cursor_thread)
cursor_thread.daemon = True
cursor_thread.start()

message = "Move the cursor to the center of the focused window when pressing Alt + Tab \n\nYou Can exit from the task tray\n"
notification.notify(title="MouseWarp is Running",message=message,app_name="MouseWarp",app_icon=resource_path("icon.ico"),timeout=2)

icon.run()