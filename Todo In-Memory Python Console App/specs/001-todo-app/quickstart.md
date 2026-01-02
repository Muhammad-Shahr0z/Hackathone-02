# Quickstart Guide: Todo Application

## Prerequisites

- Python 3.13+ installed
- UV package manager installed (for dependency management)

## Setup

1. Clone or create the project directory
2. Navigate to the project root directory
3. Install dependencies using UV:
   ```bash
   uv sync
   ```
   or if starting fresh:
   ```bash
   uv init
   ```

## Running the Application

Execute the main application file:

```bash
python src/main.py
```

Or with command arguments:

```bash
python src/main.py [command] [arguments]
```

## Available Commands

### Add a Task
```bash
python src/main.py add "Task Title" "Task Description (optional)"
```

### View All Tasks
```bash
python src/main.py view
```

### Update a Task
```bash
python src/main.py update [task_id] "New Title (optional)" "New Description (optional)"
```

### Delete a Task
```bash
python src/main.py delete [task_id]
```

### Mark Task as Complete
```bash
python src/main.py complete [task_id]
```

### Mark Task as Incomplete
```bash
python src/main.py incomplete [task_id]
```

## Example Usage

```bash
# Add a new task
python src/main.py add "Buy groceries" "Milk, eggs, bread"

# View all tasks
python src/main.py view

# Mark task #1 as complete
python src/main.py complete 1

# Update task #2
python src/main.py update 2 "Updated title" "Updated description"

# Delete task #3
python src/main.py delete 3
```