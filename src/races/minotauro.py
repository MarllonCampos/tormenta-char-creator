from src.races import base


class Minotauro(base.RacaPadrao):
    def __init__(self):
        self.displacement = 9
        self.size = "Médio"
        self.attributes = ["FOR", "FOR", "CON"]
        self.remove_attributes = ["SAB"]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def any_attribute_choices(self):
        return super().any_attribute_choices(self.except_attributes)
