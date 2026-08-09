from workflow.workflow_repository import WorkflowRepository


class WorkflowEngine:

    def __init__(self, registry):
        self.registry = registry

    def run(self):
        print("Workflow Engine is running...")

        repository = WorkflowRepository()
        workflow = repository.load_workflow()

        self.execute_workflow(workflow)

    def execute_workflow(self, workflow):
        print("Loading workflows...")

        for step in workflow:
            action = self.registry.get_action(step["action"])
            action.execute(step)