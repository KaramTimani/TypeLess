import pyautogui as pg
import time

time.sleep(5)

for i in range(3):
    pg.write("Hii")
    time.sleep(0.1)
    pg.press("Enter")
"""pg.hotkey("ctrl","a")
    pg.hotkey("ctrl","c")
    pg.press("left")
    
    pg.hotkey("ctrl","v")"""
       
