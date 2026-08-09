import subprocess

class OpenProgramAction:
    
    def execute(self,step):
        subprocess.Popen(step["program"])