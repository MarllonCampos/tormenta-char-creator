"""Tamanho Colossal"""
from .base import BaseSize


class Colossal(BaseSize):
    """Classe que contém as caracteristicas de um animal de tamanho colossal"""
    def __init__(self) -> None:
        super().__init__()
        self.colossal = "Colossal"
        self.ocuppied_space = 9
        self.natural_reach = 9
        self.furtive_modifier = -10
        self.maneuver_modifier = 10
