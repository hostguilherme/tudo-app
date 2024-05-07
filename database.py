import sqlite3

class Database:
    def __init__(self, db_file='tasks.db'):
        self.connection = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    description TEXT NOT NULL,
                    due_date TEXT,
                    priority INTEGER,
                    category TEXT
                )
                '''
            )

    def execute(self, query, params=()):
        with self.connection:
            return self.connection.execute(query, params)

    def fetchall(self, query, params=()):
        cursor = self.connection.execute(query, params)
        return cursor.fetchall()
