from src.races.base import BaseRace

from src.project_typing import Attributes


class Medusa(BaseRace):
    def __init__(self):
        self.size = Medio()
        self.attributes = [Attributes.DES, Attributes.DES, Attributes.CAR]
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    
    def cria_megalokk(self):
        # TODO -> Você é uma criatura do
        # tipo monstro e recebe visão no escuro
        pass
    
    def natureza_venenosa(self):
        # TODO ->  Você recebe resistência
        # a veneno +5 e pode gastar uma ação de movimento e
        # 1 PM para envenenar uma arma que esteja usando. A
        # arma causa perda de 1d12 pontos de vida. O veneno
        # dura até você acertar um ataque ou até o fim da cena
        # (o que acontecer primeiro). Veneno
        pass
    
    def olhar_atordoante(self):
        # TODO -> Você pode gastar uma ação de movimento e
        # 1 PM para forçar uma criatura em alcance curto a 
        # fazer um teste de Fortitude (CD Car). Se a 
        # criatura falhar, fica atordoada por uma rodada 
        # (apenas uma vez por cena)
        pass
    
    
    