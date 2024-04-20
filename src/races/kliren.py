"""Kliren"""
from src.races.base import BaseRace

from src.project_typing import Attributes


class Kliren(BaseRace):
    """Descritivo das caracteristicas da Raça Kliren"""
    def __init__(self):
        super().__init__()
        self.attributes = [Attributes.INT, Attributes.INT, Attributes.CAR]
        self.remove_attributes = [Attributes.FOR]
        self.except_attributes = None
        self.any_attribute = None
        for method in self.all_abilities():
            print(method)

    def hibrido(self):
        # TODO -> Sua natureza multifacetada fez com
        # que você aprendesse conhecimentos variados. Você
        # se torna treinado em uma prícia a sua escolha (não
        # precisa ser da sua classe)
        pass
        
    def engenhosidade(self):
        # TODO -> Quando faz um teste de
        # perícia, você pode gastar 2 PM para somar sua
        # Inteligência no teste. Você não pode usar esta
        # habilidade em testes de ataque. Caso receba esta
        # habilidade novamente, seu custo é reduzido em
        # –1 PM
        pass
    
    def ossos_frageis(self):
        # TODO -> Você sofre 1 ponto de dano adicional por 
        # dado de dano de impacto. Por exemplo, se for 
        # atingido por uma clava (dano 1d6), sofre 1d6+1
        # pontos de dano. Se cair de 3m de altura (dano 2d6), 
        # sofre 2d6+2 pontos de dano.
        pass
    
    def vanguardista(self):
        # TODO -> Você recebe proficiência em armas de
        # fogo e +2 em Ofício (um qualquer, a sua escolha).
        pass
    