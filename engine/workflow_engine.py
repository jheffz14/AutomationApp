class WorkflowEngine:

    def __init__(self, registry, logger, repository):
        self.registry = registry
        self.logger = logger
        self.repository = repository

    def run(self):

        self.logger.info("Workflow engine is running")

        workflow = self.repository.load_workflow()

        if workflow is None:
            self.logger.error("Workflow could not be loaded")
            return

        self.execute_workflow(workflow)

    def execute_workflow(self, workflow):

        self.logger.info("Loading Workflow...")

        for index, step in enumerate(workflow, start=1):

            try:

                if not self.validate_step(step):
                    return

                self.logger.info(
                    f"Step {index}: {step['action']}"
                )

                action = self.registry.get_action(
                    step["action"]
                )

                action.execute(step)

                self.logger.info(
                    f"Step {index} completed"
                )

            except ValueError as error:

                self.logger.error(f"Error: {error}")
                return
            
            except Exception as error:
                
                self.logger.error(f"Step {index} failed: {error}")
                return 
            
            
    def validate_step(self, step):
     
             action = self.registry.get_action(step["action"])
     
             for field in action.required_fields:
     
                 if field not in step:
                     print(
                         f"Error: action '{step['action']}' "
                         f"is missing required field '{field}'."
                     )
                     return False
     
             return True       