# Todo Application

A command-line todo application with in-memory storage, built with Python 3.13+.

## Setup and Installation

1. Make sure you have Python 3.13+ installed
2. Install the project dependencies:
   ```bash
   uv sync
   ```
   or if using pip:
   ```bash
   pip install -e .
   ```

## Usage

The application provides both command-line and interactive interfaces for managing todo tasks.

### Interactive Mode (Recommended)

Run the application in interactive mode to use the menu-driven interface:

```bash
python src/main.py
```

Or explicitly:

```bash
python src/main.py interactive
```

In interactive mode, you can:
- Add tasks by typing `add`
- View all tasks by typing `view`
- Update tasks by typing `update`
- Delete tasks by typing `delete`
- Mark tasks as complete by typing `complete`
- Mark tasks as incomplete by typing `incomplete`
- Get help by typing `help`
- Exit by typing `quit`

### Command-Line Mode

You can also use command-line arguments:

- **Add a task**:
  ```bash
  python src/main.py add "Task Title" "Task Description (optional)"
  ```

- **View all tasks**:
  ```bash
  python src/main.py view
  ```

- **Update a task**:
  ```bash
  python src/main.py update 1 --title "New Title" --description "New Description"
  ```

- **Delete a task**:
  ```bash
  python src/main.py delete 1
  ``

- **Mark task as complete**:
  ```bash
  python src/main.py complete 1
  ```

- **Mark task as incomplete**:
  ```bash
  python src/main.py incomplete 1
  ```

### Example Usage

```bash
# Start interactive mode
python src/main.py

# Or use command-line mode
python src/main.py add "Buy groceries" "Milk, eggs, bread"
python src/main.py view
python src/main.py complete 1
python src/main.py update 2 --title "Updated title" --description "Updated description"
python src/main.py delete 3
```

## Features

- Add tasks with titles and descriptions
- View all tasks with their status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Interactive menu-driven interface
- Command-line interface
- In-memory storage (data is lost when application closes)

## Architecture

The application follows a clean architecture pattern:

- `src/models/task.py`: Task data model
- `src/services/task_service.py`: Business logic for task operations
- `src/cli/cli.py`: Command-line interface
- `src/main.py`: Application entry point
