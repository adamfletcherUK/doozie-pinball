import yaml

try:
    from PlayfieldElements import PopBumper, SlingShot, Switch
except:
    from doozie.PlayfieldElements import PopBumper, SlingShot, Switch

class Doozie():
    def __init__(self, yaml_config):
        with open(yaml_config, "r") as stream:
            try:
                self.my_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self._init_pop_bumpers()
        self._init_slingshots()
        self._init_switches()

    def _init_pop_bumpers(self):
        self.TopLeftPop = PopBumper(self.my_dict['PopBumpers']['TopLeft'])
        self.TopRightPop = PopBumper(self.my_dict['PopBumpers']['TopRight'])
        self.CenterPop = PopBumper(self.my_dict['PopBumpers']['Center'])
        self.BottomLeftPop = PopBumper(self.my_dict['PopBumpers']['BottomLeft'])
        self.BottomRightPop = PopBumper(self.my_dict['PopBumpers']['BottomRight'])

    def _init_slingshots(self):
        self.LeftSlingshot = SlingShot(self.my_dict['Slingshots']['Left'])
        self.RightSlingshot = SlingShot(self.my_dict['Slingshots']['Right'])

    def _init_switches(self):
        #todo: define hit effects\
        #Target Switches
        self.GateTarget = Switch(self.my_dict['Switches']['Gate'])
        self.LeftOpenZipper = Switch(self.my_dict['Switches']['LeftOpenZipper'])
        self.LeftCloseZipper = Switch(self.my_dict['Switches']['LeftCloseZipper'])
        self.RightOpenZipper = Switch(self.my_dict['Switches']['RightOpenZipper'])
        self.RightCloseZipper = Switch(self.my_dict['Switches']['RightCloseZipper'])
        #Playfield Rollover Switches
        self.OneRollover = Switch(self.my_dict['Switches']['OnePlayfieldRollover'])
        self.TwoRollover = Switch(self.my_dict['Switches']['TwoPlayfieldRollover'])
        self.ThreeRollover = Switch(self.my_dict['Switches']['ThreePlayfieldRollover'])
        self.FourRollover = Switch(self.my_dict['Switches']['FourPlayfieldRollover'])
        self.FiveRollover = Switch(self.my_dict['Switches']['FivePlayfieldRollover'])
        self.FiveRolloverTop = Switch(self.my_dict['Switches']['FivePlayfieldRolloverTop'])
        #Lane Rollerover Switches
        self.OneLaneSwitch = Switch(self.my_dict['Switches']['OneLaneRollover'])
        self.TwoLaneSwitch = Switch(self.my_dict['Switches']['TwoLaneRollover'])
        self.ThreeLaneSwitch = Switch(self.my_dict['Switches']['ThreeLaneRollover'])
        self.FourLaneSwitch = Switch(self.my_dict['Switches']['FourLaneRollover'])
        #Special Switches
        self.LeftOutlaneSwitch = Switch(self.my_dict['Switches']['LeftOutlaneSwitch'])
        self.RightOutlaneSwitch = Switch(self.my_dict['Switches']['RightOutlaneSwitch'])
        self.ShooterLaneSpecialSwitch = Switch(self.my_dict['Switches']['ShooterLaneSwitch'])

    #Todo: List the things
    # Add the bumpers
    # Add the non-scoring sections
    #


if __name__ == "__main__":
    doozie = Doozie('doozie_classic_config.yaml')