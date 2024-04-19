"""Elfo"""
from src.project_typing import Attributes
from src.races.base import BaseRace



class Elfo(BaseRace):
    """Descritivo das caracteristicas da Raça Elfo"""
    def __init__(self):
        self.size = Medio()
        self.attributes = [Attributes.INT, Attributes.INT, Attributes.DES]
        self.remove_attributes = [Attributes.CON]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def graca_glorienn(self):
        # TODO -> Seu deslocamento é 12m (em vez de 9m)
        pass

    def sangue_magico(self):
        # TODO -> Você recebe +1 ponto de mana por nível.
        pass

    def sentidos_elficos(self):
        # TODO -> Você recebe visão na penumbra e +2
        # em Misticismo e Percepção.
        pass
