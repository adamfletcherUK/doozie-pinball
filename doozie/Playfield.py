import yaml
try:
    from PlayfieldElements import PopBumpers, Slingshots, Switches, RubberBumpers, \
        Lights, GameElements, TiltSwitches, Flippers
except ImportError as e:
    from doozie.PlayfieldElements import PopBumpers, Slingshots, Switches, RubberBumpers, \
        Lights, GameElements, TiltSwitches, Flippers

class Playfield():
    def __init__(self, yaml_config):
        with open(yaml_config, "r") as stream:
            try: self.my_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc: print(exc)
        self.PopBumpers = PopBumpers(self.my_dict)
        self.Slingshots = Slingshots(self.my_dict)
        self.Switches = Switches(self.my_dict)
        self.RubberBumpers = RubberBumpers(self.my_dict)
        self.Lights = Lights(self.my_dict)
        self.GameElements = GameElements(self.my_dict)
        self.TiltWitches = TiltSwitches(self.my_dict)
        self.Flippers = Flippers(self.my_dict)

    #Todo: List the things
    # Add Lights (have I got them all now)
    # Add the GameElements - Do I want to put the mechs in ??


if __name__ == "__main__":
    doozie = Playfield('doozie_classic_config.yaml')