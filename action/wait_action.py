import time


class WaitAction:

    required_fields = ["seconds"]

    def __init__(self, logger):
        self.logger = logger

    def execute(self, step):

        seconds = step.get("seconds", 2)
        
        self.logger.info(f"Waiting {seconds} seconds")

        time.sleep(seconds)