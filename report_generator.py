import sqlite3
from datetime import date 
from config import DB_PATH, TABLE_NAME

class ReportGenerator:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
    
    def get_today_sessions(self):

        today = date.today().isoformat()
        print(f"Fetching sessions for {today}...")
        
        # Connect to the database and fetch sessions for today
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            sql = f"SELECT * FROM {TABLE_NAME} WHERE date(start_time) = ?"
            cursor.execute(sql, (today,))
            sessions = cursor.fetchall()
            if not sessions:
                print("No sessions found for today.")
                return []
            
        conn.close()
            
        return sessions
    
    def get_time_spent_per_subject(self):
        
        today = date.today().isoformat()
        
        # Connect to the database and fetch time spent per subject
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            sql = f"SELECT subject, sum(work_duration) from {TABLE_NAME} where date(start_time) = ? group by subject"
            cursor.execute(sql, (today,))
            data = cursor.fetchall()
            
        conn.close()
        
        return data
        
    def generate_report(self):
        
        sessions = self.get_today_sessions()
        if not sessions:
            return "No sessions found for today."
        
        print("Today's Pomodoro Sessions:")
        for session in sessions:
            print(f"Subject: {session[3]}, Work Duration: {session[4]} minutes, Break Duration: {session[5]} minutes, Notes: {session[6]}")
        
        time_spent = self.get_time_spent_per_subject()
        print("\nTime spent per subject today:")
        for subject, time in time_spent:
            print(f"Subject: {subject}, Time Spent: {time} minutes")