"""Hynne"""
from src.races import BaseRace
from src.sizes import Pequeno
from src.project_typing import Attributes


class Hynne(BaseRace):
    """Descritivo das caracteristicas da Raça Hynne"""
    def __init__(self):
        self.size = Pequeno()
        self.attributes = [Attributes.DES, Attributes.DES, Attributes.CAR]
        self.remove_attributes = [Attributes.FOR]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def arremessador(self):
        # TODO -> Quando faz um ataque à distância com uma funda
        # ou uma arma de arremesso, seu dano aumenta em um passo.
        pass

    def pequeno_rechonchudo(self):
        # TODO -> Seu tamanho é Pequeno (veja a página 106) e
        # seu deslocamento é 6m. Você recebe +2 em Enganação e
        # pode usar Destreza como atributo-chave de Atletismo (em vez de Força)
        pass

    def sorte_salvadora(self):
        # TODO -> Quando faz um teste de resistência, você pode
        # gastar 1 PM para rolar este teste novamente.
        pass
