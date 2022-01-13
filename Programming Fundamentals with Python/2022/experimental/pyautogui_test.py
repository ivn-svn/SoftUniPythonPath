import pyautogui
testwhile = False
pyautogui.FAILSAFE = False
while not testwhile:
       # for i in range(10):  # Move mouse in a square.
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)
