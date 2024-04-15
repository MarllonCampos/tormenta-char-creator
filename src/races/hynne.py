from src.races import base


class Hynne(base.RacaPadrao):
    def __init__(self):
        self.displacement = 6
        self.size = "Pequeno"
        self.attributes = ["DES", "DES", "CAR"]
        self.remove_attributes = ["FOR"]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
