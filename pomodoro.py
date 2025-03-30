import time
import pygame as pg
import os
from session_logger import SessionLogger

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
        self.subject = subject
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
        subject = input("Enter the subject you are studying (optional): ").strip()
        if subject:
            self.subject = subject
        else:
            self.subject = "General Study"
        self.work_duration = work_duration * 60
        self.break_duration = break_duration * 60
        self.session_count = session_count
        print("Session settings updated:")
        print("Work Duration: {} minutes".format(work_duration))
        print("Break Duration: {} minutes".format(break_duration))
        print("Number of Sessions: {}".format(session_count))
        
            
    def start_session(self):
        for _ in range(self.session_count):
            print("Session {} of {}".format(_ + 1, self.session_count))
            print("Starting Pomodoro session...")
            if self.work_duration == 60:
                print("Work for 1 minute.")
            else:
                print("Work for {} minutes.".format(self.work_duration // 60))
            self.countdown(self.work_duration // 60)
            self.play_sound()
            print("Time's up! Take a break.")
            
            if self.break_duration == 60:
                print("Break for 1 minute.")
            else:
                print("Break for {} minutes.".format(self.break_duration // 60))
            self.countdown(self.break_duration // 60)
            self.play_sound()
            print("Break time is over!")
        
    def start(self):
        while True:
            self.create_session()
            print("Starting Pomodoro session...")
            self.start_session()
            print("Pomodoro session completed!")
            self.logger.log_session(self.subject, self.work_duration // 60, self.break_duration // 60, self.session_count)
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
                
            
if __name__ == "__main__":
    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.start()
