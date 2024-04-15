"""Kliren"""
from src.races import BaseRace
from src.sizes import Medio
from src.project_typing import Attributes


class Kliren(BaseRace):
    """Descritivo das caracteristicas da Raça Kliren"""
    def __init__(self):
        self.size = Medio()
        self.attributes = [Attributes.INT, Attributes.INT, Attributes.CAR]
        self.remove_attributes = [Attributes.FOR]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    
