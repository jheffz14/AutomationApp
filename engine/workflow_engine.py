from workflow.workflow_repository import WorkflowRepository
from registry.action_registry import ActionRegistry


class WorkflowEngine:
   
    def run(self):
         print("Workflow Engine is running...")     
         repository = WorkflowRepository()
         workflow = repository.load_workflow()    
         
         registry = ActionRegistry()
         
         self.execute_workflow(registry,workflow)
             
    def execute_workflow(self,registry,workflow):
        print ("Loading workflows...")
      
        for step in workflow:
            
            action = registry.get_action(step["action"])
            action.execute(step)
      
          