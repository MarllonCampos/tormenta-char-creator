"""Tamanho Enorme"""
from .base import BaseSize


class Enorme(BaseSize):
    """Classe que contém as caracteristicas de um animal de tamanho enorme"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Enorme"
        self.ocuppied_space = 4.5
        self.natural_reach = 4.5
        self.furtive_modifier = -5
        self.maneuver_modifier = 5
