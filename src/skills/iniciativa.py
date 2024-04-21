"""Tamanho Iniciativa"""
from src.project_typing import Attributes
from .base import BaseSkill


class Iniciativa(BaseSkill):
    """Classe que contém as caracteristicas da perícia Iniciativa"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Iniciativa"
        self.key_attribute = Attributes.DES
        self.description = "Esta perícia determina sua velocidade de reação em situações de perigo. Quando uma cena de ação começa, cada personagem envolvido faz um teste de Iniciativa. Eles então agem em ordem decrescente dos resultados."
