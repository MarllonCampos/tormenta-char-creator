"""Tamanho Acrobacia"""
from src.project_typing import Attributes
from .base import BaseSkill


class Acrobacia(BaseSkill):
    """Classe que contém as caracteristicas da perícia Acrobacia"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Acrobacia"
        self.key_attribute = Attributes.DES
        self.armor_penalty: bool = True
        self.description = "Você consegue fazer proezas acrobáticas."
