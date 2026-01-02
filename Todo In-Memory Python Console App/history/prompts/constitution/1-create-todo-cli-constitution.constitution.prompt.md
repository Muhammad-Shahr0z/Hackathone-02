---
id: 1
title: Create Todo CLI Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-haiku-4-5-20251001
feature: none
branch: main
user: Claude
command: /sp.constitution "Todo CLI Project Constitution / Specification"
labels: [constitution, todo, cli]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
Todo CLI Project Constitution / Specification

You are a senior Python software architect.

My project is a **Basic Level Command-Line Todo Application** built using **Python 3.13+** and **UV**.

I want you to write a **CONSTITUTION / PROJECT SPECIFICATION FILE** for this project.
The document should be professional, clean, and well structured.

### The constitution file must include the following sections:

1. **Project Overview & Objective**
2. **Scope**
   - In-memory todo application
   - No database or file persistence
3. **Technology Stack**
   - Python 3.13+
   - UV
4. **Functional Requirements**
   - Add a task (title, description)
   - View all tasks (ID, title, description, status)
   - Update task details
   - Delete a task by ID
   - Mark a task as complete or incomplete
5. **Non-Functional Requirements**
   - Clean code
   - Readability
   - Maintainability
   - Separation of concerns
6. **Data Model**
   - Task structure
   - Fields (id, title, description, status)
   - Status handling (completed / pending)
7. **CLI Interaction Flow**
   - User commands
   - Input validation
   - Console output behavior
8. **Project Structure**
   - `/src` folder containing all Python source code
   - Clear module separation (models, services, CLI handling)
   - `README.md` file with setup and run instructions
9. **Coding Standards & Clean Code Principles**
   - Meaningful naming
   - Small, focused functions
   - Single Responsibility Principle
10. **Constraints**
    - In-memory storage only
    - Console-based application
    - No external database
11. **Future Enhancements** (optional)
```

## Response snapshot

Constitution created with all required sections including:
- Core Principles (Clean Code Architecture, In-Memory Data Management, CLI-First Interaction, Test-First Development, Minimalist Design, Dependency Management with UV)
- Project Scope & Constraints (In Scope, Out of Scope, Technical Constraints)
- Data Model (Task Structure and Status Handling)
- CLI Interaction Flow (User Commands, Input Validation, Console Output Behavior)
- Project Structure (Directory Structure, Module Separation, Documentation)
- Coding Standards & Clean Code Principles (Naming Conventions, Function Design, Code Organization)
- Governance section

## Outcome

- ✅ Impact: Created comprehensive constitution file for Todo CLI project
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Ready to proceed with project implementation
- 🧠 Reflection: Constitution addresses all requirements specified by user

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A