class ActionRegistry:
    
    
    def __init__(self,actions):
        self.actions = actions

    def get_action(self,action_name):
        return self.actions.get(action_name)