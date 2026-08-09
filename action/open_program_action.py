import subprocess

class OpenProgramAction:
    
    required_fields = ["program"]
    
    def execute(self,step):
        subprocess.Popen(step["program"])