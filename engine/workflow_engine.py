import subprocess
import pyautogui
import time

class WorkflowEngine:
   
    def run(self):
         print("Workflow Engine is running...") 
         workflow = self.load_workflow()      
         self.execute_workflow(workflow)
             
    def execute_workflow(self,workflow): 
        print ("Loading workflows...")
      
        for step in workflow:
            if step["action"] == "open":
                subprocess.Popen(step["program"])
            elif step["action"] == "wait":
                time.sleep(step["seconds"])
            elif step["action"] == "type":
                pyautogui.write(step["text"], interval=0.05)
            elif step["action"] == "press":
                pyautogui.press(step["key"])
        
    
    def load_workflow(self):
              workflow = [
                        {"action": "open", "program": "notepad.exe"},
                        {"action": "wait", "seconds": 2},
                        {"action": "type", "text": "Hello Jefferson!"},
                        {"action": "press", "key": "enter"},
                        {"action": "type", "text": "Welcome to Automation Studio."}
                    ]
              return workflow