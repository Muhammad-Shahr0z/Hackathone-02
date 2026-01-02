# CLI Interface Contract

## Command Structure

### Add Task Command
- **Command**: `add`
- **Arguments**:
  - `title` (required): The title of the task
  - `description` (optional): The description of the task
- **Response**: Success message with the generated task ID
- **Error Cases**:
  - Empty title: Returns error message
  - Invalid input: Returns error message

### View Tasks Command
- **Command**: `view`
- **Arguments**: None
- **Response**: List of all tasks with ID, title, description, and status
- **Error Cases**: None (handles empty list gracefully)

### Update Task Command
- **Command**: `update`
- **Arguments**:
  - `id` (required): The ID of the task to update
  - `title` (optional): The new title of the task
  - `description` (optional): The new description of the task
- **Response**: Success message confirming update
- **Error Cases**:
  - Task ID not found: Returns error message
  - Empty title: Returns error message

### Delete Task Command
- **Command**: `delete`
- **Arguments**:
  - `id` (required): The ID of the task to delete
- **Response**: Success message confirming deletion
- **Error Cases**:
  - Task ID not found: Returns error message

### Mark Complete Command
- **Command**: `complete`
- **Arguments**:
  - `id` (required): The ID of the task to mark as complete
- **Response**: Success message confirming status change
- **Error Cases**:
  - Task ID not found: Returns error message

### Mark Incomplete Command
- **Command**: `incomplete`
- **Arguments**:
  - `id` (required): The ID of the task to mark as incomplete
- **Response**: Success message confirming status change
- **Error Cases**:
  - Task ID not found: Returns error message