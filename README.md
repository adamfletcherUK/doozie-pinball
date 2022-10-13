# Doozie Pinball

This project is to detail the restoration and conversion of the EM (Electro-Mechanical) Pinball Machine 'Doozie'

The goal of the project is to breathe new life into the Machine by replacing the EM systems (such as scoring motors and 
switch relays) with modern parts, like a computer.

The machine basically works like a computer in that it processes IF statements, stores variables, configurable variables
and creates branching paths of gameplay dependent upon the state of the game.
- The interesting point is that although this is trivial for a computer - this is all done in the pinball machine 
through motors with cams, solenoids which trip multiple switches, and variables are stored with solenoids with springs 
to hold a switch open and a reset lever, which manually closes all switches.

So my aim is to swap out these 1960s components which have a high failure rate and expert knowledge to fix, with a 
computer and microprocessors.

This should also allow me to add 'alternative game modes' and some additional quality of life improvements to add 
features like multiplayer (this pinball only supports 1 player) and persistent high scores.

## Basic Game Rules

Basic premise of the game is to hit a set of rollover switches numbered 1-5.

- There are two switches for each number, either being lane rollover switches or playfield rollover switches.
- Once all 5 switches are pressed an X lights up, light up multiple Xs and you light bonuses which award you 'free
games'. 
  - I need to figure out how best to work with this as a 'free game' on a free pinball machine is irrelevent, so might 
change this to 'add a ball'
- You get either 3 or 5 balls (depending on settings)
- When the bonus lights come on are controlled by settings
- When you have used up all your credits - there is a matching game where lights representing 0-9 light up and you have
to match that with the last digit of your score. If you match you get a free game.

I will be figuring out the entire operation of the game in order to re-create the game logic and operation in code 
(probably in Python, potentially C also if I use an Ardunio)