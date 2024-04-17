"""Raça Osteon"""
from src.races import BaseRace
from src.sizes import Medio
from src.project_typing import Attributes


class Osteon(BaseRace):
    def __init__(self):
        super().__init__()
        self.size = Medio()
        self.attributes = None
        self.remove_attributes = None
        self.except_attributes = [Attributes.CON]
        self.any_attribute = 3
        print(__class__.__name__)

    def armadura_ossea(self):
        # TODO -> Você recebe redução de corte,
        # frio e perfuração 5.
        pass

    def memoria_postuma(self):
        # TODO -> Você se torna treinado em uma perícia
        # (não precisa ser dasua classe) ou recebe um
        # poder geral a sua escolha. Como alternativa,
        # você pode ser um osteon de outra raça humanoide
        # que não humano. Neste caso, você ganha uma
        # habilidade dessa raça a sua escolha. Se a raça
        # era de tamanho diferente de Médio, você também
        # possui sua categoria de tamanho.
        pass
    
    def natureza_esqueletica(self):
        # TODO -> Você é uma criatura do tipo morto-vivo.
        # Recebe visão no escuro e imunidade a efeitos de 
        # cansaço, metabólicos, de trevas e de veneno. Além
        # disso, não precisa respirar, alimentar-se ou dormir. 
        # Por fim, efeitos mágicos de cura de luz causam dano a
        # você e você não se beneficia de itens da categoria 
        # alimentação, mas dano de trevas recupera seus PV
        pass
    
    def preço_nao_vida(self):
        # TODO -> Você precisa passar oito horas sob a luz 
        # de estrelas ou no subterrâneo. Se fizer isso, 
        # recupera PV e PM por descanso em condições normais 
        # (osteon não são afetados por condições boas ou ruins
        # de descanso). Caso contrário, sofre os efeitos de fome
        pass