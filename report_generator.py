import sqlite3
from datetime import date 

class ReportGenerator:
    def __init__(self, db_path="pomodoro_sessions.db"):
        self.db_path = db_path
    
    def get_today_sessions(self):

        today = date.today().isoformat()
        print(f"Fetching sessions for {today}...")
        
        # Connect to the database and fetch sessions for today
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sessions WHERE date(timestamp) = ?", (today,))
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
            cursor.execute("SELECT subject, sum(work_duration) from sessions where date(timestamp) = ? group by subject", (today,))
            data = cursor.fetchall()
            
        conn.close()
        
        return data
        
    def generate_report(self):
        
        sessions = self.get_today_sessions()
        if not sessions:
            return "No sessions found for today."
        
        print("Today's Pomodoro Sessions:")
        for session in sessions:
            print(f"Subject: {session[2]}, Work Duration: {session[3]} minutes, Break Duration: {session[4]} minutes, Session Count: {session[5]}, Total Time: {(session[3] + session[4]) * session[5]} minutes")
        
        time_spent = self.get_time_spent_per_subject()
        print("\nTime spent per subject today:")
        for subject, time in time_spent:
            print(f"Subject: {subject}, Time Spent: {time} minutes")