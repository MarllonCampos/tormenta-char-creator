"""Tamanho Adestramento"""
from src.project_typing import Attributes
from .base import BaseSkill


class Adestramento(BaseSkill):
    """Classe que contém as caracteristicas da perícia Adestramento"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Adestramento"
        self.key_attribute = Attributes.CAR
        self.only_trained: bool = True
        self.description = "Você sabe lidar com animais."
