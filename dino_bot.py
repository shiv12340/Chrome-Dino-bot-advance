import pyautogui
from PIL import Image, ImageGrab
import keyboard
import time


def hit(key):
    pyautogui.press(key)
    return


def iscollide(data):
      
    # Draw the rectangle for cactus
    for i in range(250, 420):
        for j in range(410, 470):
            if data[i, j] < 100:
                hit("up")
                return

    return


if __name__ == "__main__":
    print("Bot is playing!! ")
    print("Press 'q' to exit!! ")
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)
        if keyboard.is_pressed('q'):
            break

## Training part. 
##        # Draw the rectangle for cactus
##        for i in range(250, 420):
##            for j in range(410, 470):
##                data[i, j] = 0
##                    
##        image.show()
##        break
