
import json
import os


class WorkflowRepository:
    
    
    def __init__(self):
        self.workflow_file = os.path.join(os.path.dirname(__file__),"workflow.json")
    
    def load_workflow(self):
   
        with open(self.workflow_file,"r", encoding="utf-8") as file:
            workflow = json.load(file)
        return workflow 
       