"""Sulfure"""
from src.races.suraggel import Suraggel

from src.project_typing import Attributes


class Sulfure(Suraggel):
    """Descritivo das caracteristicas da Raça Sulfure"""
    def __init__(self):
        super().__init__()
        self.attributes = [Attributes.DES, Attributes.DES, Attributes.INT]
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = None
        for method in self.all_abilities():
            print(method)

    def sombras_profanas(self):
        # TODO -> Você recebe +2 em Enganação e Furtividade.
        # Além disso, pode lançar Escuridão (como uma magia
        # divina; atributo chave Inteligência). Caso 
        # aprenda novamente essa magia, seu custo diminui
        # em –1 PM.
        pass
