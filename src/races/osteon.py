from src.races import base


class Osteon(base.RacaPadrao):
    def __init__(self):
        self.displacement = 9
        self.size = "Médio"
        self.attributes = None
        self.remove_attributes = None
        self.except_attributes = ["CON"]
        self.any_attribute = 3
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
