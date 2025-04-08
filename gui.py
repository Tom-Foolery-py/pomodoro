import customtkinter as ctk 
from timer import PomodoroTimer
from session_logger import SessionLogger
from datetime import datetime
import uuid

class PomodoroApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ctk.set_default_color_theme("themes/orange.json") 
        
        self.title("Pomodoro")
        self.geometry("500x800")
        self.time_left = str(0)
        
        self.status_label = ctk.CTkLabel(
            master=self,
            text="Pomodoro Timer",
            font=("Helvetica", 48, "bold"),
        )
        
        self.status_label.pack(pady=20)
        
        # Timer variables
        self.timer_label = ctk.CTkLabel(
            master=self,
            text="00:00",
            font=("Helvetica", 48, "bold"),
        )
        self.timer_label.pack(pady=20)
        
        # Session phase variables
        self.session_phase_label = ctk.CTkLabel(
            master=self,
            text="",
            font=("Helvetica", 24, "bold"),
        )
        self.session_phase_label.pack()
        
        self.session_control_button = ctk.CTkButton(
            master=self,
            text="Start Session",
            command=self.start_session
        )
        self.session_control_button.pack(pady=100)
        
        self.logger = SessionLogger()
        
        self.current_session_group_id = ""
        
        self.pause_button = ctk.CTkButton(
            master=self,
            text="Pause",
            command=self.toggle_pause
        )
        
        self.work_duration_input_label = ctk.CTkLabel(self, text="Work Duration (minutes:")
        self.work_duration_input_label.pack()
        self.work_duration_input = ctk.CTkComboBox(self, values=["1","15", "20", "25", "30", "35", "40", "45", "50", "55", "60"])
        self.work_duration_input.set("25")
        self.work_duration_input.pack(pady=5)
        
        self.break_duration_input_label = ctk.CTkLabel(self, text="Break Duration (minutes):")
        self.break_duration_input_label.pack()
        self.break_duration_input = ctk.CTkComboBox(self, values=["1","5", "10", "15", "20"])
        self.break_duration_input.set("5")
        self.break_duration_input.pack(pady=5)
        
        self.session_count_input_label = ctk.CTkLabel(self, text="Session Count:")
        self.session_count_input_label.pack()
        self.session_count_input = ctk.CTkComboBox(self, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])
        self.session_count_input.set("4")
        self.session_count_input.pack(pady=5)
        
    def start_session(self):
        self.current_session_group_id = str(uuid.uuid4())
        
        work_duration = int(self.work_duration_input.get())
        break_duration = int(self.break_duration_input.get())
        session_count = int(self.session_count_input.get())
        
        self.status_label.configure(text="Session started!")
        self.timer = PomodoroTimer(app=self, work_duration=work_duration, break_duration=break_duration, session_count=session_count, timer_update_callback=self.update_timer_label, session_count_update_callback=self.update_session_label, phase_update_callback=self.update_phase_label, timer_complete_callback=self.on_timer_complete, work_session_complete_callback=self.on_work_session_complete, session_ready_check_callback=self.session_ready_check)
        self.hide_timer_inputs()
        self.timer.start()

        self.session_control_button.configure(text="Pause Session", command=self.toggle_pause)
        
    def countdown(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            formatted_time = f"{mins:02}:{secs:02}"
            self.timer_label.configure(text=formatted_time)
            self.time_left -= 1
            self.after(1000, self.countdown)
            print(f"Time left: {self.time_left} seconds")
        else:
            self.timer_label.configure(text="Session Complete!")
    
    def update_timer_label(self, formatted_time):
        self.timer_label.configure(text=formatted_time)
        
    def update_session_label(self, session_number):
        self.status_label.configure(text=f"Session {session_number} of {self.timer.session_count}")
        
    def update_phase_label(self, phase):
        self.session_phase_label.configure(text=phase)
            
    def on_timer_complete(self):
        self.lift()
        self.focus_force()
        
        self.status_label.configure(text="All sessions complete!")
        
        sessions_complete_popup = ctk.CTkToplevel(self)
        sessions_complete_popup.title("Sessions Complete!")
        sessions_complete_popup.geometry("500x250")
        
        sessions_complete_label = ctk.CTkLabel(sessions_complete_popup, text="All sessions complete! Would you like to start a new session?")
        sessions_complete_label.pack(pady=20)
        
        def start_new_session():
            sessions_complete_popup.destroy()
            self.session_control_button.configure(text="Start Session", command=self.start_session, state="normal")
            self.status_label.configure(text="Pomodoro Timer")
            self.session_phase_label.configure(text="")
            self.timer_label.configure(text="00:00")
            self.show_timer_inputs()
        
        def end_session():
            sessions_complete_popup.destroy()
            self.quit()
            
        new_session_btn = ctk.CTkButton(sessions_complete_popup, text="Start New Session", command=start_new_session)
        new_session_btn.pack(pady=5)
        
        exit_btn = ctk.CTkButton(sessions_complete_popup, text="Exit", command=end_session)
        exit_btn.pack(pady=5)
        
        sessions_complete_popup.grab_set()
        sessions_complete_popup.focus_force()
        
    def on_work_session_complete(self, continue_callback=None):
        self.lift()
        self.focus_force()
        
        subject_dialog = ctk.CTkInputDialog(title="Reflection", text="What subject did you work on?")
        if subject_dialog is None:
            subject = ""
        else:
            subject = subject_dialog.get_input()
        
        notes_dialog = ctk.CTkInputDialog(title="Reflection", text="Any notes/reflection for this session?")
        if notes_dialog is None:
            notes = ""
        else:
            notes = notes_dialog.get_input()
        
        self.logger.log_session(
            start_time=datetime.now().isoformat(),
            study_session_id=self.current_session_group_id,
            subject=subject,
            work_duration=self.timer.work_duration // 60,
            break_duration=self.timer.break_duration // 60,
            notes=notes
        )
        
        if continue_callback:
            continue_callback()
        
        
    def session_ready_check(self, session_type, resume_callback):
        ready_popup = ctk.CTkToplevel(self)
        ready_popup.title("Ready to start the session?")
        ready_popup.geometry("500x150")
        ready_popup.resizable(False, False)
        
        ready_label = ctk.CTkLabel(ready_popup, text=f"Are you ready to start the {session_type} session?")
        ready_label.pack(pady=20)
        
        def continue_session():
            ready_popup.destroy()
            resume_callback()
            
        ready_button = ctk.CTkButton(ready_popup, text="Ready", command=continue_session)
        ready_button.pack()
        
        ready_popup.grab_set()
        ready_popup.focus_force()
        
    def toggle_pause(self):
        paused = self.timer.toggle_pause()
        
        if paused:
            self.session_control_button.configure(text="Resume Session")
        else:
            self.session_control_button.configure(text="Pause Session")
            
    def hide_timer_inputs(self):
        self.work_duration_input_label.pack_forget()
        self.work_duration_input.pack_forget()
        self.break_duration_input_label.pack_forget()
        self.break_duration_input.pack_forget()
        self.session_count_input_label.pack_forget()
        self.session_count_input.pack_forget()

    def show_timer_inputs(self):
        self.work_duration_input_label.pack()
        self.work_duration_input.pack(pady=5)
        self.break_duration_input_label.pack()
        self.break_duration_input.pack(pady=5)
        self.session_count_input_label.pack()
        self.session_count_input.pack(pady=5)


    
    
if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()