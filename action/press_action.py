

import pyautogui


class PressAction:
    
    required_fields = ["key"]
    
    def __init__(self, logger):
        self.logger = logger
    
    def execute(self, step):
        key = step.get("key", "")
        pyautogui.press(key)