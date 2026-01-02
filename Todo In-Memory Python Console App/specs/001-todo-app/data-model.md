# Data Model: Todo Application

## Task Entity

### Fields
- **id**: `int` - Unique identifier for each task (auto-generated, sequential)
- **title**: `str` - Required title of the task (non-empty string)
- **description**: `str` - Optional description of the task (string, can be empty)
- **is_completed**: `bool` - Task completion status (True for completed, False for pending)

### Validation Rules
- `id`: Must be a positive integer, auto-generated and unique within the system
- `title`: Required field, must not be empty or contain only whitespace
- `description`: Optional field, can be empty string
- `is_completed`: Boolean value, defaults to False for new tasks

### State Transitions
- **New Task**: `is_completed = False` (default state when created)
- **Mark Complete**: `is_completed = True` (transition from pending to completed)
- **Mark Incomplete**: `is_completed = False` (transition from completed to pending)

## Task List Collection

### Structure
- **tasks**: `List[Task]` - Collection of all tasks in memory during application runtime
- **next_id**: `int` - Counter for generating the next available task ID

### Operations
- Add task: Appends new Task object to the collection
- Find task by ID: Returns Task object matching the given ID
- Update task: Modifies existing Task object in the collection
- Delete task: Removes Task object from the collection
- List all tasks: Returns all Task objects in the collection