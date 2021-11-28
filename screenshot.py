from pathlib import Path
import numpy as np
import cv2
import pyautogui
import os
   
def screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    screenshot.counter = int(readCounterVal())

    filename = Path("ss.png")

    if filename.is_file():
        filename = f"ss{str(screenshot.counter)}.png"
        screenshot.counter += 1
        writeCounterVal(str(screenshot.counter))

    cv2.imwrite(str(filename), image)

    print("Screenshot took!")

    print(os.path.abspath(str(filename)))

def writeCounterVal(value):
    f = open("counterValSS.txt", "w")

    if not Path("counterValSS.txt").is_file():
        f.write("0")
    else:
        f.write(value)

    f.close()

def readCounterVal():
    if not Path("counterValSS.txt").is_file():
        content = "0"
    else:
        f = open("counterValSS.txt", "r")
        content = f.read()
        f.close()

    return content


if __name__ == "__main__":
    screenshot()
    