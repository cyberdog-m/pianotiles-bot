import pyautogui
from time import sleep
from PIL import ImageDraw, ImageGrab, Image

#https://www.silvergames.com/en/piano-tiles

# image = ImageGrab.grab(bbox = [470,405,880,410])
# draw = ImageDraw.Draw(image)

# draw.rectangle((20,2,22,4),fill="red")
# draw.rectangle((132,2,134,4),fill="red")
# draw.rectangle((242,2,244,4),fill="red")
# draw.rectangle((362,2,364,4),fill="red")

# image.show()
sleep(1)
while True :
    image = ImageGrab.grab(bbox=[470,385,880,388])
    data = image.load()

    if data[20,2]==(0,0,0) or data[20,2]==(16,20,19) :
        pyautogui.click(490,407)
    elif data[132,2]==(0,0,0) or data[132,2]==(16,20,19):
        pyautogui.click(622,407)
    elif data[242,2]==(0,0,0) or data[242,2]==(16,20,19):
        pyautogui.click(712,407)
    elif data[362,2]==(0,0,0) or data[362,2]==(16,20,19):
        pyautogui.click(832,407)