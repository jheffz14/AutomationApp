from action.open_program_action import OpenProgramAction
from action.wait_action import WaitAction
from action.type_action import TypeAction

class ActionRegistry:
    
    
    def __init__(self):
        self.actions = {
            "open": OpenProgramAction(),
            "wait": WaitAction(),
            "type": TypeAction()
        }

    def get_action(self,action_name):
        return self.actions.get(action_name)