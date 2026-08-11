from workflow.workflow_repository import WorkflowRepository

class WorkflowEngine:

    def __init__(self, registry,logger):
        self.registry = registry
        self.logger = logger

    def run(self):

        self.logger.info("Workflow engine is running")

        repository = WorkflowRepository()

        workflow = repository.load_workflow()

        if workflow is None:
            self.logger.info("Workflow could not be loaded")
            return

        self.execute_workflow(repository, workflow)

    def execute_workflow(self, repository, workflow):

        self.logger.info("Loading Workflow...")

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

                self.logger.error(f"Error: {error}")
                return