"""Dahllan"""
from src.project_typing import Attributes
from src.races.base import BaseRace



class Dahllan(BaseRace):
    """Descritivo das caracteristicas da Raça Dahllan"""
    def __init__(self):
        self.size = Medio()
        self.attributes = [Attributes.SAB, Attributes.SAB,  Attributes.DES]
        self.remove_attributes = [Attributes.INT]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def amiga_das_plantas(self):
        # TODO -> Você pode lançar a magia
        # Controlar Plantas (atributo-chave Sabedoria). Caso
        # aprenda novamente essa magia, seu custo diminui em –1 PM.
        pass

    def armadura_alihanna(self):
        # TODO -> Você pode gastar uma ação de movimento e
        #  1 PM para transformar sua pele em casca de árvore,
        #  recebendo +2 na Defesa até o fim da cena.
        pass

    def empatia_selvagem(self):
        # TODO -> Você pode se comunicar com animais por meio de
        # linguagem corporal e vocalizações. Você pode usar Adestramento
        # para mudar atitude e persuasão com animais (veja Diplomacia,
        # na página 118). Caso receba esta habilidade novamente, recebe +2 em
        # Adestramento.
        pass
