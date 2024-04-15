"""Tamanho Pequeno"""
from .base import BaseSize


class Pequeno(BaseSize):
    """Classe que contém as caracteristicas de um animal de tamanho pequeno"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pequeno"
        self.ocuppied_space = 1.5
        self.natural_reach = 1.5
        self.furtive_modifier = 2
        self.maneuver_modifier = -2
