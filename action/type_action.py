
import pyautogui


class TypeAction:
    
   def execute(self, step):
      text = step.get("text", "")
      pyautogui.write(text, interval=0.05)