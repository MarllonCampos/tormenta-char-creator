from racas import racapadrao


class Anao(racapadrao.RacaPadrao):
    def __init__(self):
        self.displacement = 6
        self.size = "Médio"
        self.attributes = ["CON", "CON", "SAB"]
        self.remove_attributes = ["DES"]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
