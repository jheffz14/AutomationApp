from workflow.workflow_repository import WorkflowRepository


class WorkflowEngine:

    def __init__(self, registry):
        self.registry = registry

    def run(self):

        print("Workflow Engine is running...")

        repository = WorkflowRepository()

        workflow = repository.load_workflow()

        if workflow is None:
            print("Workflow could not be loaded.")
            return

        self.execute_workflow(repository, workflow)

    def execute_workflow(self, repository, workflow):

        print("Loading workflows...")

        for step in workflow:

            try:

                if not repository.validate_step(
                    step,
                    self.registry
                ):
                    return

                action = self.registry.get_action(
                    step["action"]
                )

                action.execute(step)

            except ValueError as error:

                print(f"Error: {error}")
                return