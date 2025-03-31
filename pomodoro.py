import time
import pygame as pg
import os
import uuid
from session_logger import SessionLogger
from report_generator import ReportGenerator

class PomodoroTimer:
    """
    A simple Pomodoro timer that allows the user to set work and break durations as well as number of iterations.
    The timer will count down the work duration, then prompt the user to take a break.
    After the break, it will prompt the user to start another work session.
    """
    def __init__(self, work_duration=25, break_duration=5, session_count=4, sound_file="sounds/temple_bell_002.wav", subject=None):
        self.session_count = session_count
        self.work_duration = work_duration * 60
        self.break_duration = break_duration * 60
        self.sound_file = sound_file
        self.logger = SessionLogger()
        pg.mixer.init()
        
    def countdown(self, minutes):
        seconds = minutes * 60
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
            
    def create_session(self):
        work_duration = int(input("Enter work duration in minutes (default is 25): ") or 25)
        break_duration = int(input("Enter break duration in minutes (default is 5): ") or 5)
        session_count = int(input("How many sessions do you want to complete? (default is 4): ") or 4)
        self.work_duration = work_duration * 60
        self.break_duration = break_duration * 60
        self.session_count = session_count
        print("Session settings updated:")
        print("Work Duration: {} minutes".format(work_duration))
        print("Break Duration: {} minutes".format(break_duration))
        print("Number of Sessions: {}".format(session_count))
        
            
    def start_session(self):
        session_group_id = str(uuid.uuid4())
        
        for _ in range(self.session_count):
            input("Press Enter to start the study session.")
            print("Session {} of {}".format(_ + 1, self.session_count))
            print("Starting Pomodoro session...")
            if self.work_duration == 60:
                print("Work for 1 minute.")
            else:
                print("Work for {} minutes.".format(self.work_duration // 60))
            self.countdown(self.work_duration // 60)
            self.play_sound()
            print("Time's up! Let's take a break.")
            
            subject = input("What subject did you work on? ")
            notes = input("Any notes/reflection for this session? ")
            self.logger.log_session(session_group_id, subject, self.work_duration // 60, self.break_duration // 60, notes)
            
            input("Press Enter to start your break.")
            
            if self.break_duration == 60:
                print("Break for 1 minute.")
            else:
                print("Break for {} minutes.".format(self.break_duration // 60))
            self.countdown(self.break_duration // 60)
            self.play_sound()
            print("Break time is over! Let's get back to work.")
            
        
    def run(self):
        while True:
            self.create_session()
            print("Starting Pomodoro session...")
            self.start_session()
            print("Pomodoro session completed!")
            
            view_report = input("Do you want to view today's stats? (y/n): ").strip().lower()
            if view_report == 'y':
                report_generator = ReportGenerator()
                report = report_generator.generate_report()
                print(report)
            
            again = input("Do you want to start another session? (y/n): ").strip().lower()
            if again != 'y':
                print("Exiting Pomodoro timer.")
                break
            
    def play_sound(self):
        try:
            if os.path.exists(self.sound_file):
                pg.mixer.music.load(self.sound_file)
                pg.mixer.music.play()
                while pg.mixer.music.get_busy():
                    pg.time.Clock().tick(10)
            else:
                print("Sound file not found.")
        except Exception as e:
            print(f"Error playing sound: {e}")
    
    def present_menu(self):
        print("Welcome to Pomodoro!")
        print("Pomodoro Menu")
        print("1. Start Pomodoro Session")
        print("2. View Today's Stats")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice
        
    def start(self):
        
        while True:
            choice = self.present_menu()
            
            if choice == '1':
                self.run()
            elif choice == '2':
                report_generator = ReportGenerator()
                report_generator.generate_report()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")