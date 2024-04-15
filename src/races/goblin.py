"""Goblin"""
from src.races import base
from src.sizes import Pequeno
from src.project_typing import Attributes


class Goblin(base.RacaPadrao):
    """Descritivo das caracteristicas da Raça Goblin"""
    def __init__(self):
        self.size = Pequeno()
        self.attributes = [Attributes.DES, Attributes.DES, Attributes.INT]
        self.remove_attributes = [Attributes.CAR]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def engenhoso(self):
        # TODO -> Você não sofre penalidades em
        # testes de perícia por não usar ferramentas. Se usar a
        # ferramenta necessária, recebe +2 no teste de perícia.
        pass

    def espelunqueiro(self):
        # TODO -> Você recebe visão no escuro
        # e deslocamento de escalada igual ao seu deslocamento terrestre.
        pass

    def peste_esguia(self):
        # TODO -> Seu tamanho é Pequeno (veja apágina 106),
        #  mas seu deslocamento se mantém 9m.
        # Apesar de pequenos, goblins são rápidos.
        pass

    def rato_das_ruas(self):
        # TODO -> Você recebe +2 em Fortitude e sua recuperação
        # de PV e PM nunca é inferior ao seu nível.
        pass
