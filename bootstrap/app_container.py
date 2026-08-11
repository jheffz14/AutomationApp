from registry.action_registry import ActionRegistry
from logger.workflow_logger import WorkflowLogger
from config.actions import ACTIONS


class AppContainer:
    
    def __init__(self):
         self.actions = self.get_actions()
         self.registry = ActionRegistry(self.actions)
         self.logger = WorkflowLogger()
   
    def get_actions(self):
        
        actions = {}
        
        for action_name, action_class in ACTIONS.items():

         actions[action_name] = action_class()

        return actions    