"""Minotauro"""
from src.races import BaseRace
from src.sizes import Medio
from src.project_typing import Attributes


class Minotauro(BaseRace):
    """Descritivo das caracteristicas da Raça Minotauro"""
    def __init__(self):
        self.size = Medio()
        self.attributes = [Attributes.FOR, Attributes.FOR, Attributes.CON]
        self.remove_attributes = [Attributes.SAB]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def chifres(self):
        # TODO -> Você possui uma arma natural dechifres (dano 1d6,
        # crítico x2, perfuração). Uma vez por rodada, quando usa a ação
        # agredir para atacar com outra arma, pode gastar
        # 1 PM para fazer um ataque corpo a corpo extra com os chifres.
        pass

    def couro_rigido(self):
        # TODO -> Sua pele é dura como a de um touro. Você recebe +1 na Defesa.
        pass

    def faro(self):
        # TODO -> Você tem olfato apurado. Contra inimigos em alcance
        # curto que não possa ver, você não fica desprevenido e camuflagem
        # total lhe causa apenas 20% de chance de falha.
        pass

    def medo_altura(self):
        # TODO -> Se estiver adjacente a uma queda de 3m ou mais
        # de altura (como um buraco ou penhasco), você fica abalado.
        pass
