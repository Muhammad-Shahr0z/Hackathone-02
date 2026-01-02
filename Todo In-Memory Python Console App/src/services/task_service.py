from typing import List, Optional
from models.task import Task


class TaskService:
    """
    Business logic for task operations.
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.
        Returns the created task with a unique ID.
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        task = Task(id=self.next_id, title=title.strip(), description=description.strip() if description else "")
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task by its ID.
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        # Use existing values if not provided
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description

        # Validate the new title if it's being updated
        if title is not None and (not new_title or not new_title.strip()):
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Update the task
        task.title = new_title.strip() if new_title else ""
        task.description = new_description.strip() if new_description else ""

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        Returns True if the task was found and deleted, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        Returns True if the task was found and updated, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.is_completed = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.
        Returns True if the task was found and updated, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.is_completed = False
            return True
        return False