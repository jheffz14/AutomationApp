import subprocess
from action.base_action import BaseAction

class OpenProgramAction(BaseAction):
    
    required_fields = ["program"]
    
    def execute(self,step):
        program = step["program"]
        
        self.logger.info(f"Opening program: {program}")
        
        subprocess.Popen(program)