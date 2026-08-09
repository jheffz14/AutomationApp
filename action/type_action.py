
import pyautogui


class TypeAction:
    
   required_fields = ["text"]
    
   def execute(self, step):
      text = step.get("text", "")
      pyautogui.write(text, interval=0.05)