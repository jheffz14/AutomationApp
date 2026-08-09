import time

class WaitAction:

    def execute(self, step):
        seconds = step.get("seconds", 2)
        time.sleep(seconds)