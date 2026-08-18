
from engine.workflow_engine import WorkflowEngine
from bootstrap.app_container import AppContainer

def main():
    container = AppContainer()
    engine = WorkflowEngine(container.registry, container.logger,container.repository)
    engine.run()

if __name__ == "__main__":
    main()