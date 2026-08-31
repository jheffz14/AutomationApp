import time
from action.base_action import BaseAction



class WaitAction(BaseAction):

    required_fields = ["seconds"]


    def execute(self, step):

        seconds = step.get("seconds", 2)
        
        self.logger.info(f"Waiting {seconds} seconds")

        time.sleep(seconds)