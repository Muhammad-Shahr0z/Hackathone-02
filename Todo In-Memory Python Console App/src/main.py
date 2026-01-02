from services.task_service import TaskService
from cli.cli import CLI


def main():
    """
    Main application entry point.
    """
    # Initialize the task service and CLI
    task_service = TaskService()
    cli = CLI(task_service)

    # Run the CLI
    cli.run()


if __name__ == "__main__":
    main()