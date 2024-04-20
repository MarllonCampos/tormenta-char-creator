"""Lefou"""
from src.races.base import BaseRace

from src.project_typing import Attributes


class Lefou(BaseRace):
    """Descritivo das caracteristicas da Raça Lefou"""
    def __init__(self):
        super().__init__()
        self.attributes = None
        self.remove_attributes = [Attributes.CAR]
        self.except_attributes = [Attributes.CAR]
        self.any_attribute = 3
        for method in self.all_abilities():
            print(method)

    def cria_tormenta(self):
        # TODO -> Você é uma criatura do tipo monstro e recebe +5 em testes de 
        # resistência contra efeitos causados por lefeu e pela Tormenta.
        pass

    def deformidade(self):
        # TODO -> Todo lefou possui defeitos físicos que, embora desagradáveis,
        # conferem certas vantagens. Você recebe +2
        # em duas perícias a sua escolha.
        # Cada um desses bônus conta como um poder da Tormenta
        # (exceto para perda de Carisma).
        # Você pode trocar um desses bônus por um poder da Tormenta
        # a sua escolha (ele também não conta para perdade Carisma).
        pass
