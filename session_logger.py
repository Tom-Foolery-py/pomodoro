import sqlite3
from datetime import datetime

class SessionLogger:
    
    def __init__(self, db_path='pomodoro_sessions.db'):
        self.db_path = db_path
        self._init_db()
        
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    subject TEXT,
                    work_duration INTEGER NOT NULL,
                    break_duration INTEGER NOT NULL,
                    session_count INTEGER NOT NULL
                )
            ''')
            
            conn.commit()
            
    def log_session(self, subject, work_duration, break_duration, session_count):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO sessions (timestamp, subject, work_duration, break_duration, session_count)
                VALUES (?, ?, ?, ?, ?)
            ''', (datetime.now().isoformat(), subject, work_duration, break_duration, session_count))
            
            conn.commit()
            
        print("Session logged successfully.")
            
    