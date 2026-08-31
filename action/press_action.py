import pyautogui
from action.base_action import BaseAction


class PressAction(BaseAction):
    
    required_fields = ["key"]
    
    def execute(self, step):
        key = step.get("key", "")
        self.logger.info(f"Pressing: {key}")
        pyautogui.press(key)