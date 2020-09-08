import pyautogui
from time import sleep
from PIL import ImageDraw, ImageGrab, Image

#https://www.silvergames.com/en/piano-tiles


sleep(1)
while True :
    if pyautogui.pixel(490,387)[0]==0 or pyautogui.pixel(490,387)[0]==16:
        pyautogui.click(490,407)
    elif pyautogui.pixel(602,387)[0]==0 or pyautogui.pixel(602,387)[0]==16:
        pyautogui.click(622,407)
    elif pyautogui.pixel(712,387)[0]==0 or pyautogui.pixel(712,387)[0]==16:
        pyautogui.click(712,407)
    elif pyautogui.pixel(832,387)[0]==0 or pyautogui.pixel(832,387)[0]==16:
        pyautogui.click(832,407)
    