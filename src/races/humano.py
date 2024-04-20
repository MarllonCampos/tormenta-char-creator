"""Humano"""
from src.races.base import BaseRace

class Humano(BaseRace):
    """Descritivo das caracteristicas da Raça Humano"""
    def __init__(self):
        super().__init__()
        self.add_attributes = None
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = 3
        for method in self.all_abilities():
            print(method)

    def versatil(self):
        # TODO -> Criar uma classe de Pericias e permitir escolher 2
        # pericias quaisquer
        pass
