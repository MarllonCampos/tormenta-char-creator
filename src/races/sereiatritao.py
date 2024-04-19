"""Raça Sereia Tritão"""
from src.races.base import BaseRace



class SereiaTritao(BaseRace):
    def __init__(self):
        super().__init__()
        self.size = Medio()
        self.attributes = None
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = 3
        print(__class__.__name__)

    def cancao_mares(self):
        # TODO -> Você pode lançar duas das magias
        # a seguir: Amedrontar, Comando, Despedaçar, Enfeitiçar,
        # Hipnotismo ou Sono (atributo-chave Carisma). Caso
        # aprenda novamente uma dessas magias, seu custo diminui em –1 PM
        pass

    def mestre_tridente(self):
        # TODO -> Para você, o tridente é uma arma simples.
        # Além disso, você recebe +2 em rolagens de dano
        # com azagaias, lanças e tridentes
        pass

    def transformacao_anfibia(self):
        # TODO -> Você pode respirar debaixo d’água e
        # possui uma cauda que fornece deslocamento de
        # natação 12m. Quando fora d’água, sua cauda
        # desaparece e dá lugar a pernas (deslocamento 9m).
        # Se permanecer mais de um dia sem contato com água,
        # você não recupera PM com descanso até voltar para a
        # água (ou, pelo menos, tomar um bom banho!)
        pass
