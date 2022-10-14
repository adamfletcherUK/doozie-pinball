# Gameplay

## Start Playing The Game

- After money has been put into the machine you'll get credits, which will be shown on the replay 
dial (I'll cover this in another section) #TODO
- You then press the play button.
- This knocks the ball out of the ball trough and into the shooter lane.
  - there is a switch in the ball trough
- There is a switch to determine if it is there.
- You launch the ball using a launcher (to electronic parts)


## Playfield Overview
- At the top there are 4 lane rollover switches (1-4) 
- and one playfield rollover switch (5)
  - Hitting any of these will award 


## Pop Bumper Lighting and Scoring
- There are 5 pop bumpers (2 yellow, 2 red and 1 green)
  - Yellows and Reds are worth 1 point when unlit and 10 points when lit
  - The Green is worth 10 points when unlit and 100 points when lit

## Specials
Need to check the frequency of the specials depending on the settings from the plug in the backbox.
See if they match the Excel I found.

### Gate Special
- Available on 2 consecutive of 2X-5X depending upon settings (verified)
- Setup: When lit, open the gate by hitting the switch
- Claim by: Hitting the ball through the gate and activating the launch roller switch
- Reward: 1 Replay
- Finally: Special light will turn off and cannot be claimed until next X

### Autoreplay Special (Making Next X scores special)
- Available on 2 (with 1 gap) [verified] of 3X-7X depending upon settings [backbox looks like between 4 and 8]
- Setup: You need to progress to the next X
- Claim by: Progressing to the next X
- Reward: 1 Replay
- Finally: Special light will turn off and cannot be claimed until next X

### Outlane Special (Rollover Special)
- Available on 2 or 1 of 4X-7X depending upon settings [Verified]
- Setup: The game will randomly decide which outlane to light
- Claim by: Losing the ball down the outlanes
- Reward: 1 replay
- Finally: Special light will turn off and cannot be claimed until next X

## 1-5 Lights
- When lit score = `10`
- When unlit score = `1`
- **^^ IS THIS CORRECT^^**

## Scoring Settings
- `True**` denotes True dependent upon Adjuster!
- `True^^` denotes if the switch is set to liberal, if not False

**This doesn't take into account physical parts moving which I might want to add to keep feel authentic**

### 0X:
- Red Pops [`lit = True`, `points = 10`]
- Yellow Pops [`lit = True`, `points = 10`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = False`, `autoreplay = False`, `outlane = False`]
- Lights [`None`]

### 1X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = True`, `points = 100`]
- Bumpers [`points = 1`]
- Specials [`gate = False`, `autoreplay = False`, `outlane = False`]
- Lights [`1X`]

### 2X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = True`, `points = 10`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = True**`, `autoreplay = False`, `outlane = False`]
- Lights [`2X`]

### 3X:
- Red Pops [`lit = True`, `points = 10`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = True**`, `autoreplay = True**`, `outlane = False`]
- Lights [`3X`]

### 4X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = True^^`, `points = 100`]
- Bumpers [`points = 1`]
- Specials [`gate = True**`, `autoreplay = True**`, `outlane = True**`]
- Lights [`4X`]

### 5X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = True**`, `autoreplay = True**`, `outlane = True**`]
- Lights [`5X`]

### 6X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = False`, `autoreplay = True**`, `outlane = True**`]
- Lights [`6X`]

### 7X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = False`, `autoreplay = True**`, `outlane = True**`]
- Lights [`7X`]

### 8X:
- Red Pops [`lit = False`, `points = 1`]
- Yellow Pops [`lit = False`, `points = 1`]
- Green Pop [`lit = False`, `points = 10`]
- Bumpers [`points = 1`]
- Specials [`gate = False`, `autoreplay = False`, `outlane = False`]
- Lights [`8X`]
- Notes: Does this just reset to 0? does it score a replay??


## Misc
- When the ball drains the zipper flippers reset to normal position
- playfiel rollerover switches are 100 points
- how much are targets?

### Playfield Mechanical Parts
- 9 wire rollover switches
- 6 plastic rollover switches
- 5 targets
- 5 pop bumpers
- 1 mechanical gate
- 4 bumper switches
- 4 slingshot switches
- 2 slingshot coils
- 2 flipper coils
- 2 flipper switches
- 2 zipper flipper coils
- 1 ball through coil
- 37 bulbs

### Backbox Parts
- 46 bulbs
- 1 replay reel (2 coils)
- 4 score reels (4 coils)

### Sounds
- 2 bell coils
- 1 knocker

### Tilt Mechs

### Coin Door Mechs

### Misc
- 1 total play meter
- Any of the physical mechs I want to keep to sound authentic
