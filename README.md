# MazeBot
About: Based on the seminal 1951 work 'Theseus The Mouse' by Claude Shannon, MazeBot navigates a reconfigurable 5x5 cell maze. 
Hardware: core XY 3-axis CNC platform
Programs in repository:
  maze_play.py: main program which creates 11x11 matrix and populates it based on feedback from machine electrically sensing maze walls.
  manager.py: runs when machine is booted up and sequentially calls on sub routines based on user input through four tactile switches. Displays output to user through RGB LEDs. Also handles errors and shutdown.
  raise.py: program to raise probe from maze. Called by manager based on certain tactile switch input sequence.
  lower.py: program to lower probe into maze. Called by manager based on certain tactile switch input sequence.
Read more: https://jblevoy.wixsite.com/skunkworks/mazebot
Watch more: https://jblevoy.wixsite.com/skunkworks/mazebot-video
