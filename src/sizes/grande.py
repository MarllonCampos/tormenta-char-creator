"""Tamanho Grande"""
from .base import BaseSize


class Grande(BaseSize):
    """Classe que contém as caracteristicas de um animal de tamanho grande"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Grande"
        self.ocuppied_space = 3
        self.natural_reach = 3
        self.furtive_modifier = -2
        self.maneuver_modifier = 2
