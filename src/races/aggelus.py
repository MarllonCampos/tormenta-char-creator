"""Aggelus"""
from src.races import BaseRace
from src.sizes import Medio
from src.project_typing import Attributes


class Aggelus(BaseRace):
    """Descritivo das caracteristicas da Raça Aggelus"""
    def __init__(self):
        self.size = Medio()
        self.attributes = [Attributes.SAB, Attributes.SAB, Attributes.CAR]
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def luz_sagrada(self):
        # TODO -> Você recebe +2 em Diplomacia e Intuição.
        # Além disso, pode lançar Luz (como uma magia divina;
        # atributo-chave Carisma). Caso aprenda novamente
        # essa magia, seu custo diminui em –1 PM
        pass
