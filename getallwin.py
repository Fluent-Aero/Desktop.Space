from win32 import win32gui
import time

def get():
    hwnds = {}
    effective_hwnds = []
    effective_hts = {}

    def get_all_hwnd(hwnd, mouse):
    	if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
		    hwnds[hwnd] = win32gui.GetWindowText(hwnd)

    win32gui.EnumWindows(get_all_hwnd, 0)
    for i in hwnds:
        if(hwnds[i]!=""):
            effective_hts[i] = str(hwnds[i])
    return effective_hts
