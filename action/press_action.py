

import pyautogui


class PressAction:
    
    required_fields = ["key"]
    
    def execute(self, step):
        key = step.get("key", "")
        pyautogui.press(key)