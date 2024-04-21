"""Tamanho Conhecimento"""
from src.project_typing import Attributes
from .base import BaseSkill


class Conhecimento(BaseSkill):
    """Classe que contém as caracteristicas da perícia Conhecimento"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Conhecimento"
        self.key_attribute = Attributes.INT
        self.only_trained = True
        self.description = "Você estudou diversos campos do saber, como aritmética, astronomia, dialética, geografia, história..."
