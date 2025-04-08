# Pomodoro Clock

Pomodoro is a simple but powerful technique to maintain focus during study or work. By structuring sessions with intentional breaks and minimizing distractions, you can enter deep flow states and get more done.

I built this app using the Pomodoro method itself — and ironically, overshot a few sessions just from how effective the method is. So grab a tea, toss your phone in a vault, and enter sigma grindset ultra-study mode.

For more information on the Pomodoro technique, see [here](https://en.wikipedia.org/wiki/Pomodoro_Technique#:~:text=The%20Pomodoro%20Technique%20is%20a,used%20while%20a%20university%20student.&text=Apps%20and%20websites%20providing%20timers,adopted%20in%20pair%20programming%20contexts.).

---

## Motivation

Most Pomodoro apps felt bloated — requiring logins, sending data somewhere, or being overly minimal. I just wanted something simple, personal, and effective, but with a few enhancements.

Also:
- Microsoft’s Focus Mode never tracked properly in my experience
- I wanted a **fully offline**, **customizable** Pomodoro timer
- I needed a way to **log reflection notes** and **track subjects** for future review
- A desktop application allows for an "out of sight, out of mind" approach as I will most likely use the internet during any sort of studying being done and having Pomodoro open in a browser tab or window creates an additional distraction

This app is built for internal use, but it’s also a portfolio piece that reflects my approach to tools: **purposeful, mindful, and personal**.

---

## Features

- GUI-based Pomodoro timer (built with CustomTkinter)
- SQLite-based session logging (only logs completed work sessions)
- Subject tracking per session
- Reflection notes for journaling and review

---

## Planned Enhancements

- Theme customization
- In-app analytics dashboard
- More robust tracking and reporting
- Theme catalog system for swappable UI moods
- Overall UX. Since I'll be using this daily, there will be changes here and there that offers me a better experience

---

## What I Learned

- **State management and event-driven architecture** — especially separating GUI logic from timer logic using callbacks
- That I learn far more from **building real tools** than passively consuming books or videos
- That I know nothing. 

---

## Version

**Current:** `1.0.0` — MVP with full session flow and logging

---

## Installation

Ensure you have Python installed (3.10+ recommended).

```bash
git clone https://github.com/Tom-Foolery-py/pomodoro.git
cd pomodoro
pip install -r requirements.txt
python main.py
```