import subprocess
import pyautogui
import time
from workflow.workflow_repository import WorkflowRepository

class WorkflowEngine:
   
    def run(self):
         print("Workflow Engine is running...")     
         repository = WorkflowRepository()
         workflow = repository.load_workflow()    
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
        
    
    