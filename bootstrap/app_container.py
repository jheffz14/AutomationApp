from action.open_program_action import OpenProgramAction
from action.wait_action import WaitAction
from action.type_action import TypeAction
from action.press_action import PressAction
from registry.action_registry import ActionRegistry


class AppContainer:
    
    def __init__(self):
         self.actions = {
                    "open": OpenProgramAction(),
                    "wait": WaitAction(),
                    "type": TypeAction(),
                    "press": PressAction()
                }
         self.registry = ActionRegistry(self.actions)
   