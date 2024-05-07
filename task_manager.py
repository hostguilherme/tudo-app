from database import Database

class TaskManager:
    def __init__(self):
        self.db = Database()

    def add_task(self, description, due_date, priority, category):
        query = 'INSERT INTO tasks (description, due_date, priority, category) VALUES (?, ?, ?, ?)'
        self.db.execute(query, (description, due_date, priority, category))

    def view_tasks(self):
        query = 'SELECT * FROM tasks ORDER BY due_date'
        return self.db.fetchall(query)

    def edit_task(self, task_id, description=None, due_date=None, priority=None, category=None):
        if description:
            self.db.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
        if due_date:
            self.db.execute('UPDATE tasks SET due_date = ? WHERE id = ?', (due_date, task_id))
        if priority is not None:
            self.db.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, task_id))
        if category:
            self.db.execute('UPDATE tasks SET category = ? WHERE id = ?', (category, task_id))

    def delete_task(self, task_id):
        self.db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
