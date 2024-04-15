from src.races import BaseRace
from src.project_typing import Sizes

class Humano(BaseRace):
    def __init__(self):
        self.size = Sizes.MEDIO
        self.attributes = None
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = 3
        print(__class__.__name__)
