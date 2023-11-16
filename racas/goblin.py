from racas import racapadrao


class Goblin(racapadrao.RacaPadrao):
    def __init__(self):
        self.displacement = 9
        self.size = "Pequeno"
        self.attributes = ["DES", "DES", "INT"]
        self.remove_attributes = ["CAR"]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
