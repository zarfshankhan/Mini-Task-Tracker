# Mini Task Tracker

## Project Description
Mini Task Tracker is a menu-based Python application that helps users manage their daily tasks. Users can add, view, complete, and delete tasks. The application uses a JSON file to save tasks and load them when the program runs again.

## Features
- **Add Task:** Add a new task with a title.
- **View Tasks:** Display all tasks with their status (Pending or Done).
- **Complete Task:** Mark a task as completed.
- **Delete Task:** Remove a task from the list.
- **Save Tasks:** Store tasks in `tasks.json`.
- **Load Tasks:** Load previously saved tasks when the program starts.
- **Error Handling:** Handle empty titles, invalid menu choices, invalid task numbers, and missing JSON files.
- **Menu-Based Interface:** Keep displaying the menu until the user selects Exit.

## Technologies Used
- Python
- JSON
- GitHub

## Project Files

```text
mini-task-tracker/
├── mini_task_tracker.py
├── tasks.json
└── README.md
```

- `mini_task_tracker.py` — Contains the main Python program.
- `tasks.json` — Stores tasks and their completion status.
- `README.md` — Provides project documentation.

## How to Run the Project

### Using a Computer

1. Install Python.
2. Download the project files from GitHub.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python mini_task_tracker.py
   ```

## Example Output

```text
--- TASK TRACKER ---
1. Add
2. View
3. Complete
4. Delete
5. Exit

Choice: 1
Task title: Read notes
Task added.

Choice: 2
1. Read notes [Pending]

Choice: 3
1. Read notes [Pending]
Task number: 1
Task completed.

Choice: 2
1. Read notes [Done]

Choice: 5
Tasks saved. Goodbye!
```

## JSON Data Format

Tasks are stored in `tasks.json` in JSON format.

Example:

```json
[
    {
        "title": "Read notes",
        "done": false
    },
    {
        "title": "Complete Python assignment",
        "done": true
    }
]
```

- `title` stores the task description.
- `done` stores the completion status (`false` for Pending and `true` for Done).

## Error Handling

The program handles:
- Empty task titles.
- Invalid menu choices.
- Invalid task numbers.
- Non-numeric task numbers.
- Missing or invalid JSON files.

## Data Persistence

The program saves tasks to `tasks.json` whenever a task is added, completed, or deleted. It loads saved tasks at startup so they remain available when the program is restarted, provided the JSON file is preserved.

**Note:** In Google Colab, files may be lost when the runtime resets. Download your files or save them to Google Drive to preserve them between sessions.

## Learning Outcomes

This project demonstrates:
- Python functions.
- Lists and dictionaries.
- Loops and conditional statements.
- User input and output.
- File handling.
- JSON serialization and deserialization.
- Exception handling.

## Author

Zarfshan Attiq Khan