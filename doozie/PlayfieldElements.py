class PlayfieldElement:
    def __init__(self, config_dict):
        self.type = config_dict['type']
        self.name = config_dict['name']
        self.led_color = 'White'
        self.light_address = None
        self.switch_pin = None
        self.relay_pin = None
        self.points_lit = config_dict['points_lit']
        self.points_unlit = config_dict['points_unlit']
        self.is_lit = config_dict['starts_lit']

    def score_points(self):
        # TODO: Add a tally to score points
        return self.points_lit if self.is_lit else self.points_unlit

    def hit_effect(self):
        return None


class SinglePopBumper(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)
        self.physical_colour = config_dict['color']


class SingleSlingShot(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)


class SingleSwitch(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)


class PopBumpers:
    def __init__(self, config_dict):
        self.TopLeftPop = SinglePopBumper(config_dict['PopBumpers']['TopLeft'])
        self.TopRightPop = SinglePopBumper(config_dict['PopBumpers']['TopRight'])
        self.CenterPop = SinglePopBumper(config_dict['PopBumpers']['Center'])
        self.BottomLeftPop = SinglePopBumper(config_dict['PopBumpers']['BottomLeft'])
        self.BottomRightPop = SinglePopBumper(config_dict['PopBumpers']['BottomRight'])


class Slingshots:
    def __init__(self, config_dict):
        self.LeftSlingshot = SingleSlingShot(config_dict['Slingshots']['Left'])
        self.RightSlingshot = SingleSlingShot(config_dict['Slingshots']['Right'])


class Switches:
    def __init__(self, config_dict):
        #Target Switches
        self.GateTarget = SingleSwitch(config_dict['Switches']['Gate'])
        self.LeftOpenZipper = SingleSwitch(config_dict['Switches']['LeftOpenZipper'])
        self.LeftCloseZipper = SingleSwitch(config_dict['Switches']['LeftCloseZipper'])
        self.RightOpenZipper = SingleSwitch(config_dict['Switches']['RightOpenZipper'])
        self.RightCloseZipper = SingleSwitch(config_dict['Switches']['RightCloseZipper'])
        #Playfield Rollover Switches
        self.OneRollover = SingleSwitch(config_dict['Switches']['OnePlayfieldRollover'])
        self.TwoRollover = SingleSwitch(config_dict['Switches']['TwoPlayfieldRollover'])
        self.ThreeRollover = SingleSwitch(config_dict['Switches']['ThreePlayfieldRollover'])
        self.FourRollover = SingleSwitch(config_dict['Switches']['FourPlayfieldRollover'])
        self.FiveRollover = SingleSwitch(config_dict['Switches']['FivePlayfieldRollover'])
        self.FiveRolloverTop = SingleSwitch(config_dict['Switches']['FivePlayfieldRolloverTop'])
        #Lane Rollerover Switches
        self.OneLaneSwitch = SingleSwitch(config_dict['Switches']['OneLaneRollover'])
        self.TwoLaneSwitch = SingleSwitch(config_dict['Switches']['TwoLaneRollover'])
        self.ThreeLaneSwitch = SingleSwitch(config_dict['Switches']['ThreeLaneRollover'])
        self.FourLaneSwitch = SingleSwitch(config_dict['Switches']['FourLaneRollover'])
        #Special Switches
        self.LeftOutlaneSwitch = SingleSwitch(config_dict['Switches']['LeftOutlaneSwitch'])
        self.RightOutlaneSwitch = SingleSwitch(config_dict['Switches']['RightOutlaneSwitch'])
        self.ShooterLaneSpecialSwitch = SingleSwitch(config_dict['Switches']['ShooterLaneSwitch'])

