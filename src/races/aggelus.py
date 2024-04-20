"""Aggelus"""
from src.races.suraggel import Suraggel

from src.project_typing import Attributes


class Aggelus(Suraggel):
    """Descritivo das caracteristicas da Raça Aggelus"""
    def __init__(self):
        super().__init__()
        self.attributes = [Attributes.SAB, Attributes.SAB, Attributes.CAR]
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = None
        for method in self.all_abilities():
            print(method)

    def luz_sagrada(self):
        # TODO -> Você recebe +2 em Diplomacia e Intuição.
        # Além disso, pode lançar Luz (como uma magia divina;
        # atributo-chave Carisma). Caso aprenda novamente
        # essa magia, seu custo diminui em –1 PM
        pass
