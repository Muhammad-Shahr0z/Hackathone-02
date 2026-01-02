import argparse
from typing import List, Optional
from services.task_service import TaskService


class CLI:
    """
    Command-line interface for the todo application.
    """

    def __init__(self, task_service: TaskService):
        self.task_service = task_service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create the argument parser with all available commands.
        """
        parser = argparse.ArgumentParser(
            description="Todo CLI Application - Manage your tasks from the command line"
        )
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("title", help="Task title", nargs='?')
        add_parser.add_argument("description", nargs="?", default="", help="Task description (optional)")

        # View command
        view_parser = subparsers.add_parser("view", help="View all tasks")

        # Update command
        update_parser = subparsers.add_parser("update", help="Update a task")
        update_parser.add_argument("id", type=int, help="Task ID", nargs='?')
        update_parser.add_argument("--title", help="New task title (optional)")
        update_parser.add_argument("--description", help="New task description (optional)")

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("id", type=int, help="Task ID", nargs='?')

        # Complete command
        complete_parser = subparsers.add_parser("complete", help="Mark task as complete")
        complete_parser.add_argument("id", type=int, help="Task ID", nargs='?')

        # Incomplete command
        incomplete_parser = subparsers.add_parser("incomplete", help="Mark task as incomplete")
        incomplete_parser.add_argument("id", type=int, help="Task ID", nargs='?')

        # Interactive mode
        subparsers.add_parser("interactive", help="Run in interactive mode")

        return parser

    def run(self, args: List[str] = None):
        """
        Run the CLI with the given arguments.
        """
        # If no arguments provided or if 'interactive' command is specified, run in interactive mode
        if not args or (args and len(args) > 0 and args[0] == 'interactive'):
            self._run_interactive()
        else:
            parsed_args = self.parser.parse_args(args)
            self._handle_command(parsed_args)

    def _handle_command(self, parsed_args):
        """
        Handle a specific command based on parsed arguments.
        """
        if parsed_args.command == "add":
            # If title wasn't provided in command line, ask interactively
            if not parsed_args.title:
                title = input("Enter task title: ").strip()
                description = input("Enter task description (optional): ").strip()
                self._handle_add_interactive(title, description)
            else:
                self._handle_add(parsed_args)
        elif parsed_args.command == "view":
            self._handle_view()
        elif parsed_args.command == "update":
            # If task ID wasn't provided in command line, ask interactively
            if not parsed_args.id:
                task_id = int(input("Enter task ID to update: "))
                title = input("Enter new title (or press Enter to keep current): ").strip() or None
                description = input("Enter new description (or press Enter to keep current): ").strip() or None
                self._handle_update_interactive(task_id, title, description)
            else:
                self._handle_update(parsed_args)
        elif parsed_args.command == "delete":
            # If task ID wasn't provided in command line, ask interactively
            if not parsed_args.id:
                task_id = int(input("Enter task ID to delete: "))
                self._handle_delete_interactive(task_id)
            else:
                self._handle_delete(parsed_args)
        elif parsed_args.command == "complete":
            # If task ID wasn't provided in command line, ask interactively
            if not parsed_args.id:
                task_id = int(input("Enter task ID to mark complete: "))
                self._handle_complete_interactive(task_id)
            else:
                self._handle_complete(parsed_args)
        elif parsed_args.command == "incomplete":
            # If task ID wasn't provided in command line, ask interactively
            if not parsed_args.id:
                task_id = int(input("Enter task ID to mark incomplete: "))
                self._handle_incomplete_interactive(task_id)
            else:
                self._handle_incomplete(parsed_args)
        else:
            self._run_interactive()

    def _run_interactive(self):
        """
        Run the application in interactive mode with a menu.
        """
        print("Welcome to the Todo Application!")
        print("Type 'help' for available commands or 'quit' to exit.\n")

        while True:
            try:
                command = input("Enter command (add/view/update/delete/complete/incomplete/quit): ").strip().lower()

                if command == 'quit' or command == 'exit':
                    print("Goodbye!")
                    break
                elif command == 'help':
                    self._show_help()
                elif command == 'add':
                    self._interactive_add()
                elif command == 'view':
                    self._handle_view()
                elif command == 'update':
                    self._interactive_update()
                elif command == 'delete':
                    self._interactive_delete()
                elif command == 'complete':
                    self._interactive_complete()
                elif command == 'incomplete':
                    self._interactive_incomplete()
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def _show_help(self):
        """
        Show help information.
        """
        print("\nAvailable commands:")
        print("  add        - Add a new task")
        print("  view       - View all tasks")
        print("  update     - Update a task")
        print("  delete     - Delete a task")
        print("  complete   - Mark task as complete")
        print("  incomplete - Mark task as incomplete")
        print("  quit       - Exit the application")
        print("  help       - Show this help message")
        print()

    def _interactive_add(self):
        """
        Interactive task addition.
        """
        title = input("Enter task title: ").strip()
        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional): ").strip()

        try:
            task = self.task_service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    def _interactive_update(self):
        """
        Interactive task update.
        """
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.\n")
            return

        # Get the current task to show current values
        current_task = self.task_service.get_task_by_id(task_id)
        if not current_task:
            print(f"Error: Task with ID {task_id} not found.\n")
            return

        print(f"Current title: {current_task.title}")
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        new_title = new_title if new_title else None  # Keep as current if empty

        print(f"Current description: {current_task.description}")
        new_description = input("Enter new description (or press Enter to keep current): ").strip()
        new_description = new_description if new_description else None  # Keep as current if empty

        try:
            result = self.task_service.update_task(task_id, new_title, new_description)
            if result:
                print(f"Task {task_id} updated successfully\n")
            else:
                print(f"Error: Task with ID {task_id} not found\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    def _interactive_delete(self):
        """
        Interactive task deletion.
        """
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.\n")
            return

        result = self.task_service.delete_task(task_id)
        if result:
            print(f"Task {task_id} deleted successfully\n")
        else:
            print(f"Error: Task with ID {task_id} not found\n")

    def _interactive_complete(self):
        """
        Interactive marking task as complete.
        """
        try:
            task_id = int(input("Enter task ID to mark complete: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.\n")
            return

        result = self.task_service.mark_complete(task_id)
        if result:
            print(f"Task {task_id} marked as complete\n")
        else:
            print(f"Error: Task with ID {task_id} not found\n")

    def _interactive_incomplete(self):
        """
        Interactive marking task as incomplete.
        """
        try:
            task_id = int(input("Enter task ID to mark incomplete: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.\n")
            return

        result = self.task_service.mark_incomplete(task_id)
        if result:
            print(f"Task {task_id} marked as incomplete\n")
        else:
            print(f"Error: Task with ID {task_id} not found\n")

    def _handle_add(self, args):
        """
        Handle the add command (non-interactive).
        """
        try:
            task = self.task_service.add_task(args.title, args.description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_add_interactive(self, title: str, description: str = ""):
        """
        Handle the add command with interactive input.
        """
        try:
            task = self.task_service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_view(self, args=None):
        """
        Handle the view command.
        """
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print("\nID  | Title                  | Description           | Status")
        print("--- | ---------------------- | --------------------- | ------")
        for task in tasks:
            status = "✓ Completed" if task.is_completed else "○ Pending"
            # Truncate long titles and descriptions for display
            title = task.title[:20] + "..." if len(task.title) > 20 else task.title
            desc = task.description[:19] + "..." if len(task.description) > 19 else task.description
            print(f"{task.id:<3} | {title:<22} | {desc:<19} | {status}")
        print()

    def _handle_update(self, args):
        """
        Handle the update command (non-interactive).
        """
        try:
            result = self.task_service.update_task(args.id, args.title, args.description)
            if result:
                print(f"Task {args.id} updated successfully")
            else:
                print(f"Error: Task with ID {args.id} not found")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_update_interactive(self, task_id: int, title: Optional[str], description: Optional[str]):
        """
        Handle the update command with interactive input.
        """
        try:
            result = self.task_service.update_task(task_id, title, description)
            if result:
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_delete(self, args):
        """
        Handle the delete command (non-interactive).
        """
        result = self.task_service.delete_task(args.id)
        if result:
            print(f"Task {args.id} deleted successfully")
        else:
            print(f"Error: Task with ID {args.id} not found")

    def _handle_delete_interactive(self, task_id: int):
        """
        Handle the delete command with interactive input.
        """
        result = self.task_service.delete_task(task_id)
        if result:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def _handle_complete(self, args):
        """
        Handle the complete command (non-interactive).
        """
        result = self.task_service.mark_complete(args.id)
        if result:
            print(f"Task {args.id} marked as complete")
        else:
            print(f"Error: Task with ID {args.id} not found")

    def _handle_complete_interactive(self, task_id: int):
        """
        Handle the complete command with interactive input.
        """
        result = self.task_service.mark_complete(task_id)
        if result:
            print(f"Task {task_id} marked as complete")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def _handle_incomplete(self, args):
        """
        Handle the incomplete command (non-interactive).
        """
        result = self.task_service.mark_incomplete(args.id)
        if result:
            print(f"Task {args.id} marked as incomplete")
        else:
            print(f"Error: Task with ID {args.id} not found")

    def _handle_incomplete_interactive(self, task_id: int):
        """
        Handle the incomplete command with interactive input.
        """
        result = self.task_service.mark_incomplete(task_id)
        if result:
            print(f"Task {task_id} marked as incomplete")
        else:
            print(f"Error: Task with ID {task_id} not found")