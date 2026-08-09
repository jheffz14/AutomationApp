

import pyautogui


class PressAction:
    
    def execute(self, step):
        key = step.get("key", "")
        pyautogui.press(key)