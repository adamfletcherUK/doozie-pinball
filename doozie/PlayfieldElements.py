class PlayfieldElement():
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
        #TODO: Add a tally to score points
        return self.points_lit if self.is_lit else self.points_unlit

    def hit_effect(self):
        return None

class PopBumper(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)
        self.physical_colour = config_dict['color']

class SlingShot(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)

class Switch(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)

class RubberBumper(PlayfieldElement):
    def __init__(self, config_dict):
        super().__init__(config_dict)