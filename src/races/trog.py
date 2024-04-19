"""Trog"""

from src.races.base import BaseRace

from src.project_typing import Attributes
class Trog(BaseRace):
    def __init__(self):
        """Descritivo das caracteristicas da Raça Trog"""        

        self.attributes = [Attributes.CON, Attributes.CON, Attributes.FOR]
        self.remove_attributes = [Attributes.INT]
        self.except_attributes = None
        self.any_attribute = None
        first_method = self.all_methods()[0]

        method = getattr(self,first_method)
        method()


    def mau_cheiro(self):
        # TODO -> Você pode gastar uma ação padrão e 2 PM para 
        #    expelir um gás fétido. 
        #    Todas as criaturas (exceto trogs) em alcance curto 
        #    devem passar em um teste de Fortitude contra veneno 
        #    (CD Con) ou ficarão enjoadas durante 1d6 rodadas. Uma
        #    criatura que passe no teste de resistência fica imune
        #    a esta habilidade por um dia.
        print("Mau Cheiro")
        pass

    def mordida(self):
        # TODO -> Você possui uma arma natural de
        # mordida (dano 1d6, crítico x2, perfuração). Uma
        # vez por rodada, quando usa a ação agredir para
        # atacar com outra arma, pode gastar 1 PM para fazer
        # um ataque corpo a corpo extra com a mordida.
        pass

    def reptiliano(self):
        # TODO -> Você é uma criatura do tipo
        # monstro e recebe visão no escuro, +1 na Defesa
        # e, se estiver sem armadura ou roupas pesadas,
        # +5 em Furtividade
        pass

    def sangue_frio(self):
        # TODO -> Você sofre 1 ponto de dano adicional
        # por dado de dano de frio.
        pass
