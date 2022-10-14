import yaml

class PlayfieldElement():
    ...

class PopBumper():
    def __init__(self, config_dict):
        self.colour = config_dict['color']
        self.points_lit = config_dict['points_lit']
        self.points_unlit = config_dict['points_unlit']
        self.is_lit = False
        self.relay_pin = None
        self.light_pin = None


class Doozie():
    def __init__(self, yaml_config):
        with open(yaml_config, "r") as stream:
            try:
                self.my_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        self.TopLeftPop = PopBumper(self.my_dict['PopBumpers']['TopLeft'])


    def thing(self):
        ...

if __name__ == "__main__":
    doozie = Doozie('doozie_classic_config.yaml')
    print(doozie.TopLeftPop.points_lit)