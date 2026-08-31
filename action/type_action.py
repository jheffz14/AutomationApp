import pyautogui
from action.base_action import BaseAction

class TypeAction(BaseAction):
    
   required_fields = ["text"]
    
   def execute(self, step):
      text = step.get("text", "")
      
      self.logger.info(f"Typing: {text}")
      pyautogui.write(text, interval=0.05)