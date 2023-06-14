import os
import pyautogui
import time

def main():
    os.system('start runrage.bat')
    print("START RAGE MP")
    time.sleep(15)

    # connection

    pyautogui.moveTo(1357, 216)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(1116,560)
    pyautogui.click()

    print('CONNECTION TO SERVER')

    time.sleep(10)

    pyautogui.moveTo(1120, 621)
    pyautogui.click()

    time.sleep(600)

    print('GTA V RUNNING')

    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(581, 994)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1111, 968)
    pyautogui.click()
    time.sleep(60)

    print("LOGGED TO SERVER")

    time.sleep(20000)
    os.system('shutdown -s -t 60')

    print("FINISH")
