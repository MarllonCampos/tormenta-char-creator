from src.races import base


class Medusa(base.RacaPadrao):
    def __init__(self):
        self.displacement = 9
        self.size = "Médio"
        self.attributes = ["DES", "DES", "CAR"]
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
