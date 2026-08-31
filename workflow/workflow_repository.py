import json
import os


class WorkflowRepository:

    def __init__(self,logger):
        self.logger = logger
        
        self.workflow_file = os.path.join(
            os.path.dirname(__file__),
            "workflow.json"
        )

    def load_workflow(self):

        with open(
            self.workflow_file,
            "r",
            encoding="utf-8"
        ) as file:

            workflow = json.load(file)

        if not self.validate_workflow(workflow):
            return None

        return workflow

    def validate_workflow(self, workflow):

        if not isinstance(workflow, list):
            self.logger.error("Workflow must be a list of steps")
            return False

        for step in workflow:

            if not isinstance(step, dict):
                self.logger.error("Workflow must be an object")
                return False

            if "action" not in step:
                self.logger.error("Workflow step is missing 'action'")
                return False

        return True


    