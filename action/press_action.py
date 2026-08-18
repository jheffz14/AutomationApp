

import pyautogui


class PressAction:
    
    required_fields = ["key"]
    
    def __init__(self, logger):
        self.logger = logger
    
    def execute(self, step):
        key = step.get("key", "")
        self.logger.info(f"Pressing: {key}")
        pyautogui.press(key)