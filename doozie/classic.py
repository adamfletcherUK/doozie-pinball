import yaml
from Playfield import Playfield

playfield = Playfield('./doozie_classic_config.yaml')

class Game:
    def __init__(self):
        self.x = 0
        self.score = 0
        self.ball_in_play = 0
        self.ball_count = 5
        self.Xmap = {0: None,
                1: '1X',
                2: '2X',
                3: '3X',
                4: '4X',
                5: '5X',
                6: '6X',
                7: '7X',
                8: '8X'}
        self.centerpopmap = {0: False,
                             1: True,
                             2: False,
                             3: True,
                             4: False,
                             5: False,
                             6: False,
                             7: False,
                             8: False}
        self.progress_switches = [0,0,0,0,0]

game = Game()
playfield = Playfield('doozie_classic_config.yaml')

def switch_status():
    print(f'OneLane: {playfield.Switches.OneLaneSwitch.is_lit}\n'
          f'OneRollover: {playfield.Switches.OneRollover.is_lit}\n'
          f'TwoLane: {playfield.Switches.TwoLaneSwitch.is_lit}\n'
          f'TwoRollover: {playfield.Switches.TwoRollover.is_lit}\n'
          f'ThreeLane: {playfield.Switches.ThreeLaneSwitch.is_lit}\n'
          f'ThreeRollover: {playfield.Switches.ThreeRollover.is_lit}\n'
          f'FourLane: {playfield.Switches.FourRollover.is_lit}\n'
          f'FourRollover: {playfield.Switches.FourRollover.is_lit}\n'
          f'FiveRolloverTop: {playfield.Switches.FiveRolloverTop.is_lit}\n'
          f'FiveRolover: {playfield.Switches.FiveRollover.is_lit}\n'
          f'')
    return None

## Showing filling in the switches to light Xs
# for i in range(0, 15, 1):
#     if 0 not in game.progress_switches:
#         print('All Switches Triggered')
#         game.x = (game.x + 1) if game.x < 8 else 0 #this isn't quite right
#         game.progress_switches = [0,0,0,0,0]
#         print(game.x)
#     for s in range(0,5,1):
#         game.progress_switches[s] = 1
#         print(game.progress_switches)


## Showing how I can change the points value based on the X count
for i in range(1, 10):
    print(game.score)
    if 0 not in game.progress_switches:
        print('All Switches Triggered')
        game.x = (game.x + 1) if game.x < 8 else 0 #this isn't quite right
        game.progress_switches = [0,0,0,0,0]
        playfield.PopBumpers.CenterPop.is_lit = game.centerpopmap[game.x]
        print(game.x)
    for s in range(0,5,1):
        game.progress_switches[s] = 1
        # print(game.progress_switches)
    game.score += playfield.PopBumpers.CenterPop.score_points()

