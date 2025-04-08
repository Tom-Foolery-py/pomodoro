class PomodoroTimer:
    
    def __init__(self, app, work_duration=25, break_duration=5, session_count=4, sound_file="sounds/temple_bell_002.wav", timer_update_callback=None, session_count_update_callback=None, phase_update_callback=None, timer_complete_callback=None, work_session_complete_callback=None, session_ready_check_callback=None):
        
        self.app = app
        self.session_count = session_count
        self.work_duration = work_duration * 60
        self.break_duration = break_duration * 60
        self.sound_file = sound_file
        
        self.timer_update_callback = timer_update_callback
        self.timer_complete_callback = timer_complete_callback
        self.session_count_update_callback = session_count_update_callback
        self.phase_update_callback = phase_update_callback
        self.work_session_complete_callback = work_session_complete_callback
        self.session_ready_check_callback = session_ready_check_callback
        
        self.is_break = False
        self.current_session = 0
        self.time_left = self.work_duration
        
        self.paused = False
    
    def start(self):
        self.current_session = 1
        self.is_break = False
        self.time_left = self.work_duration
        
        if self.phase_update_callback:
            self.phase_update_callback("Work")
        
        if self.session_count_update_callback:
            self.session_count_update_callback(self.current_session)
        
        self._tick()
    
    def _tick(self):
        if self.timer_update_callback:
            mins, secs = divmod(self.time_left, 60)
            formatted_time = f"{mins:02}:{secs:02}"
            self.timer_update_callback(formatted_time)
        
        if self.time_left > 0:
            if not self.paused:
                self.time_left -= 1
            self.app.after(1000, self._tick)
        else:
            if not self.is_break:
                self.is_break = True
                
                if self.work_session_complete_callback:
                    self.work_session_complete_callback()
                
                if self.phase_update_callback:
                    self.phase_update_callback("Break")
                    
                self.time_left = self.break_duration
                
                if self.session_ready_check_callback:
                    self.session_ready_check_callback("Break", lambda: self.app.after(1000, self._tick))
                else:  
                    self.app.after(1000, self._tick)
                    
            else:
                self.current_session += 1
                
                if self.current_session <= self.session_count:
                    if self.session_count_update_callback:
                        self.session_count_update_callback(self.current_session)
                    self.is_break = False
                    self.time_left = self.work_duration
                    
                    if self.phase_update_callback:
                        self.phase_update_callback("Work")
                        
                    if self.session_ready_check_callback:
                        self.session_ready_check_callback("Work", lambda: self.app.after(1000, self._tick))
                    else:
                        self.app.after(1000, self._tick)
                else:
                    if self.timer_complete_callback:
                        self.timer_complete_callback()
                
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
        
    def toggle_pause(self):
        self.paused = not self.paused
        return self.paused