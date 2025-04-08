# Pomodoro Clock

Pomodoro is a simple but powerful technique to maintain focus during study or work. By structuring sessions with intentional breaks and minimizing distractions, you can enter deep flow states and get more done.

I built this app using the Pomodoro method itself — and ironically, overshot a few sessions just from how effective the method is. So grab a tea, toss your phone in a vault, and enter sigma grindset ultra-study mode.

---

## Motivation

Most Pomodoro apps felt bloated — requiring logins, sending data somewhere, or being overly minimal. I just wanted something simple, personal, and effective, but with a few enhancements.

Also:
- Microsoft’s Focus Mode never tracked properly in my experience
- I wanted a **fully offline**, **customizable** Pomodoro timer
- I needed a way to **log reflection notes** and **track subjects** for future review

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

---

## What I Learned

- **State management and event-driven architecture** — especially separating GUI logic from timer logic using callbacks
- That I learn far more from **building real tools** than passively consuming books or videos
- That I know nothing. (Yet.)

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