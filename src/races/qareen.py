"""Qareen"""
from src.races.base import BaseRace

from src.project_typing import Attributes


class Qareen(BaseRace):
    """Descritivo das caracteristicas da Raça Qareen"""
    def __init__(self):
        super().__init__()
        self.attributes = [Attributes.CAR, Attributes.CAR, Attributes.INT]
        self.remove_attributes = [Attributes.SAB]
        self.except_attributes = None
        self.any_attribute = None
        for method in self.all_abilities():
            print(method)

    def desejos(self):
        # TODO -> Se lançar uma magia que alguém tenha pedido desde
        # seu último turno, o custo da magia diminui em –1 PM.
        # Fazer um desejo ao qareen é uma ação livre.
        pass

    def resistencia_elemental(self):
        # TODO -> Conforme sua ascendência, você recebe redução 10 a um tipo de
        # dano. Escolha uma: frio (qareen da água), eletricidade (do ar),
        # fogo (do fogo), ácido (da terra), luz (da luz)
        # ou trevas (qareen das trevas).
        pass

    def tatuagem_mistica(self):
        # TODO -> Você pode lançar uma magia de 1º círculo
        # a sua escolha (atributo-chave Carisma). Caso aprenda novamente essa
        # magia, seu custo diminui em –1 PM.
        pass
