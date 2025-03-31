# Pomodoro Clock

## Motivation 
A Pomodoro clock seemed simple enough to build on my own rather than using others. The key reason I wanted to do this was because a lot of the apps require users to log-in or provide information for use. I wanted more control over my own data in this regard. It also seemed like a learning opportunity for myself. I actually wanted to work on something else but got sidetracked on this project so that I can use it for a different project.

## Features
- Custom Command-line Pomodoro timer
- Bell alert notification using Pygame
- SQLite-based session logging (only completed work sessions)
- Subject tracking per session
- Session reporting for the day

## Next features/enhancements
- GUI
- Theme catalog
- More comprehensive analytics
- In-app analytics view
- Re-factoring to break up responsibilities. Pomodoro script is taking too many responsibilities. Building a separate sessions class that handles all session activity. 

## Version

Current: `0.1.0` - CLI-only prototype, usable for daily studying

## Acknowledgments 
- [temple_bell_002.wav](https://freesound.org/people/tec_studio/sounds/668647/) by [tec_studio](https://freesound.org/people/tec_studio/)