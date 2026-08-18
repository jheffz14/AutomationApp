
import pyautogui


class TypeAction:
    
   required_fields = ["text"]
    
   def __init__(self, logger):
    self.logger = logger
    
   def execute(self, step):
      text = step.get("text", "")
      
      self.logger.info(f"Typing: {text}")
      pyautogui.write(text, interval=0.05)