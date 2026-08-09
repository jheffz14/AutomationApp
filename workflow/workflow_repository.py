

class WorkflowRepository:
    
    def load_workflow(self):
   
        
        workflow = [
                {"action": "open", "program": "notepad.exe"},
                {"action": "wait", "seconds": 2},
                {"action": "type", "text": "Hello Jefferson!"},
                {"action": "press", "key": "enter"},
                {"action": "type", "text": "Welcome to Automation Studio."}
                    ]
        return workflow