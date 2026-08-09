import json
import os


class WorkflowRepository:

    def __init__(self):
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
            print("Error: workflow must be a list of steps.")
            return False

        for step in workflow:

            if not isinstance(step, dict):
                print("Error: workflow step must be an object.")
                return False

            if "action" not in step:
                print("Error: workflow step is missing 'action'.")
                return False

        return True


    def validate_step(self, step, registry):

        action = registry.get_action(step["action"])

        for field in action.required_fields:

            if field not in step:
                print(
                    f"Error: action '{step['action']}' "
                    f"is missing required field '{field}'."
                )
                return False

        return True