class ActionRegistry:
    
    
    def __init__(self,actions):
        self.actions = actions

    def get_action(self,action_name):
        action =  self.actions.get(action_name)
        
        if action is None:
          raise ValueError(f"Action '{action_name}' is not registered.")
        return action