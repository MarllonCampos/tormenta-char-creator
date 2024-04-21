"""Tamanho Jogatina"""
from src.project_typing import Attributes
from .base import BaseSkill


class Jogatina(BaseSkill):
    """Classe que contém as caracteristicas da perícia Jogatina"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Jogatina"
        self.key_attribute = Attributes.CAR
        self.only_trained = True
        self.description = "Você sabe jogar jogos de azar."
