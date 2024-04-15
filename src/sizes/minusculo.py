"""Tamanho Minusculo"""
from .base import BaseSize


class Minusculo(BaseSize):
    """Classe que contém as caracteristicas de um animal de tamanho\r
    minusculo"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Minusculo"
        self.ocuppied_space = 1.5
        self.natural_reach = 1.5
        self.furtive_modifier = +5
        self.maneuver_modifier = -5
