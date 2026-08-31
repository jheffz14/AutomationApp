class BaseAction:
    
    required_fields = []
    
    def __init__(self,logger):
        self.logger = logger
        
    def execute(self, step):
        raise NotImplementedError("Action must implement execute()")    