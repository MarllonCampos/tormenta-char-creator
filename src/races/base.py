from typing import List
from src.project_typing import Attributes
from src.project_typing import Sizes

class BaseRace():

    def __init__(self):
        self.increase_attribute: List[Attributes] = None
        self.reduce_attributes: List[Attributes] = None
        self.cant_choose_attributes: List[Attributes] = None
        self.any_attribute: int = None
        self.size: Sizes = None 
