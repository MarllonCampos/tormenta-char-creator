"""Anão"""
from src.project_typing import Attributes
from src.races import BaseRace
from src.sizes import Medio


class Anao(BaseRace):
    """Descritivo das caracteristicas da Raça Anão"""
    def __init__(self):
        self.size = Medio
        self.add_attributes = [Attributes.CON, Attributes.CON, Attributes.SAB]
        self.remove_attributes = [Attributes.DES]
        self.except_attributes = None
        self.any_attribute = None

    def conhecimento_das_rochas(self):
        # TODO -> Você recebe visão no escuro e +2 em testes de
        # Percepção e Sobrevivência realizados no subterrâneo.
        pass

    def devagar_sempre(self):
        # TODO -> Seu deslocamento é 6m (em vez de 9m). Porém, seu
        # deslocamento não é reduzido por uso de armadura
        # ou excesso de carga.
        pass

    def duro_como_pedra(self):
        # TODO -> Você recebe +3 pontos de vida no 1º nível e +1 por
        # nível seguinte.
        pass

    def tradicao_heredrimm(self):
        # TODO -> Você é peri-
        # to nas armas tradicionais anãs, seja por ter treinado com elas,
        # seja por usá-las como ferramentas de ofício. Para você,
        # todos os machados, martelos, marretas e picaretas são armas
        # simples. Você recebe+2 em ataques comessas armas.
        pass
