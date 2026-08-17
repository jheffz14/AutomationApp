import subprocess

class OpenProgramAction:
    
    required_fields = ["program"]
    
    def __init__(self, logger):
        self.logger = logger
    
    def execute(self,step):
        program = step["program"]
        
        self.logger.info(f"Opening program: {program}")
        
        subprocess.Popen(program)