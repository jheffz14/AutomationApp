
from engine.workflow_engine import WorkflowEngine
from bootstrap.app_container import AppContainer

def main():
    container = AppContainer()
    engine = WorkflowEngine(container.registry)
    engine.run()

if __name__ == "__main__":
    main()