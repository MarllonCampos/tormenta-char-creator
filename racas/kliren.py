from racas import racapadrao


class Kliren(racapadrao.RacaPadrao):
    def __init__(self):
        self.displacement = 9
        self.size = "Médio"
        self.attributes = ["INT", "INT", "CAR"]
        self.remove_attributes = ["FOR"]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
