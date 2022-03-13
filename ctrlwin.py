import win32con
from win32 import win32gui
from PIL import Image, ImageGrab
import getwinsize as gws

class wc:
    def close(i):
        win32gui.PostMessage(i, win32con.WM_CLOSE, 0, 0)
    def shownormal(i):
        win32gui.ShowWindow(i,win32con.SW_SHOWNORMAL)
    def minn(i):
        win32gui.ShowWindow(i,win32con.SW_SHOWMINIMIZED)
    def maxx(i):
        win32gui.ShowWindow(i,win32con.SW_SHOWMAXIMIZED)
    def focus(i):
        win32gui.ShowWindow(i,win32con.SW_SHOW)
    def findfocus():
        return win32gui.GetForegroundWindow()
    def getwindowsize(i):
        return win32gui.GetWindowRect(i)
    def getwindowname(i):
        return win32gui.GetWindowText(i)
    def mrwindow(i,x,y,w=-1,h=-1):
        rect = win32gui.GetWindowRect(i)
        if(w==-1):
            w=rect.right-rect.left
        if(h==-1):
            h=rect.bottom-rect.top
        win32gui.MoveWindow(i,x,y,w,h,True)
    def clip(x,y,xw,yh):
        return ImageGrab.grab((x,y,xw,yh))
    def tl(i):
        win32gui.SetWindowPos(i, win32con.HWND_TOPMOST, *gws.gcs(i),win32con.SWP_SHOWWINDOW)
    def untl(i):
        win32gui.SetWindowPos(i, win32con.HWND_TOP,*gws.gcs(i), win32con.SWP_SHOWWINDOW)