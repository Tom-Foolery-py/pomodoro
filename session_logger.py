import sqlite3
from datetime import datetime
from config import DB_PATH, TABLE_NAME

class SessionLogger:
    
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._init_db()
        
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            sql = f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    pomodoro_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    study_session_id INTEGER,
                    start_time TEXT NOT NULL,
                    subject TEXT,
                    work_duration INTEGER NOT NULL,
                    break_duration INTEGER NOT NULL,
                    notes TEXT
                )
            '''
            c.execute(sql)
            
            conn.commit()
            
    def log_session(self, study_session_id, subject, work_duration, break_duration, notes):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            sql = f'''
                INSERT INTO {TABLE_NAME} (study_session_id, start_time, subject, work_duration, break_duration, notes)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            c.execute(sql, (study_session_id ,datetime.now().isoformat(), subject, work_duration, break_duration, notes))
            
            conn.commit()
            
        print("Session logged successfully.")
            
    