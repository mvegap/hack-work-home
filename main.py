import pyautogui
import time
import math

R = 350

def init():
    print("Hack work from home...")

    pyautogui.FAILSAFE = False
    while True:
        time.sleep(5)
        (x,y) = pyautogui.size()
        (X,Y) = pyautogui.position(x/2,y/2)
        pyautogui.moveTo(X+R,Y)

        for i in range(360):
            if i%6==0:
                pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))

        # print("Ok... it's moving...")
        # for i in range(0, 100):
        #     pyautogui.moveTo(0, i * 5)
        # print("Paused")


if __name__ == '__main__':
    init()
