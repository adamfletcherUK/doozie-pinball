import yaml
try: from PlayfieldElements import SingleSwitch, PopBumpers, Slingshots, Switches
except: from doozie.PlayfieldElements import SingleSwitch, PopBumpers, Slingshots, Switches

class Playfield():
    def __init__(self, yaml_config):
        with open(yaml_config, "r") as stream:
            try: self.my_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc: print(exc)
        self.PopBumpers = PopBumpers(self.my_dict)
        self.Slingshots = Slingshots(self.my_dict)
        self.Switches = Switches(self.my_dict)

        # self._init_switches()
        # self._init_rubber_bumpers()


    # def _init_switches(self):
    #     #todo: define hit effects\
    #     #Target Switches
    #     self.GateTarget = SingleSwitch(self.my_dict['Switches']['Gate'])
    #     self.LeftOpenZipper = SingleSwitch(self.my_dict['Switches']['LeftOpenZipper'])
    #     self.LeftCloseZipper = SingleSwitch(self.my_dict['Switches']['LeftCloseZipper'])
    #     self.RightOpenZipper = SingleSwitch(self.my_dict['Switches']['RightOpenZipper'])
    #     self.RightCloseZipper = SingleSwitch(self.my_dict['Switches']['RightCloseZipper'])
    #     #Playfield Rollover Switches
    #     self.OneRollover = SingleSwitch(self.my_dict['Switches']['OnePlayfieldRollover'])
    #     self.TwoRollover = SingleSwitch(self.my_dict['Switches']['TwoPlayfieldRollover'])
    #     self.ThreeRollover = SingleSwitch(self.my_dict['Switches']['ThreePlayfieldRollover'])
    #     self.FourRollover = SingleSwitch(self.my_dict['Switches']['FourPlayfieldRollover'])
    #     self.FiveRollover = SingleSwitch(self.my_dict['Switches']['FivePlayfieldRollover'])
    #     self.FiveRolloverTop = SingleSwitch(self.my_dict['Switches']['FivePlayfieldRolloverTop'])
    #     #Lane Rollerover Switches
    #     self.OneLaneSwitch = SingleSwitch(self.my_dict['Switches']['OneLaneRollover'])
    #     self.TwoLaneSwitch = SingleSwitch(self.my_dict['Switches']['TwoLaneRollover'])
    #     self.ThreeLaneSwitch = SingleSwitch(self.my_dict['Switches']['ThreeLaneRollover'])
    #     self.FourLaneSwitch = SingleSwitch(self.my_dict['Switches']['FourLaneRollover'])
    #     #Special Switches
    #     self.LeftOutlaneSwitch = SingleSwitch(self.my_dict['Switches']['LeftOutlaneSwitch'])
    #     self.RightOutlaneSwitch = SingleSwitch(self.my_dict['Switches']['RightOutlaneSwitch'])
    #     self.ShooterLaneSpecialSwitch = SingleSwitch(self.my_dict['Switches']['ShooterLaneSwitch'])

    # def _init_rubber_bumpers(self):
    #     self.TopLeftBumper = SingleRubberBumper(self.my_dict['Bumpers']['TopLeftBumper'])
    #     self.TopRightBumper = SingleRubberBumper(self.my_dict['Bumpers']['TopRightBumper'])
    #     self.MidLeftBumper = SingleRubberBumper(self.my_dict['Bumpers']['MidLeftBumper'])
    #     self.MidRightBumper = SingleRubberBumper(self.my_dict['Bumpers']['MidRightBumper'])
    #     self.BottomLeftBumper = SingleRubberBumper(self.my_dict['Bumpers']['BottomLeftBumper'])
    #     self.BottomRightBumper = SingleRubberBumper(self.my_dict['Bumpers']['BottomRightBumper'])


    #Todo: List the things
    # Add the bumpers
    # Add the non-scoring sections
    #


if __name__ == "__main__":
    doozie = Playfield('doozie_classic_config.yaml')