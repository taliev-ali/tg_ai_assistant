import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            user_id INTEGER,
            task TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_task(user_id: int, task: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (user_id, task, timestamp)
        VALUES (?, ?, ?)
    ''', (user_id, task, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_tasks(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT task FROM tasks
        WHERE user_id = ?
        ORDER BY timestamp DESC
    ''', (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
