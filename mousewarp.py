import win32gui
import win32api
import win32con
import time

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

active_hwnd = None
hwnd = None

while True:
    time.sleep(0.1)
    if win32api.GetAsyncKeyState(win32con.VK_MENU) & 0x8000:
        while win32api.GetAsyncKeyState(win32con.VK_MENU) & 0x8000:
            time.sleep(0.1)
        hwnd = get_active()
        if active_hwnd != hwnd: 
            move_mouse(hwnd)
            active_hwnd = get_active()
