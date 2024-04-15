from src.races import base


class Elfo(base.RacaPadrao):
    def __init__(self):
        self.displacement = 12
        self.size = "Médio"
        self.attributes = ["INT", "INT", "DES"]
        self.remove_attributes = ["CON"]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
