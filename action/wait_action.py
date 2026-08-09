import time

class WaitAction:
    
    required_fields = ["seconds"]
    
    def execute(self, step):
        seconds = step.get("seconds")
        time.sleep(seconds)