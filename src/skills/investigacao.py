"""Tamanho Investigação"""
from src.project_typing import Attributes
from .base import BaseSkill


class Investigacao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Investigação"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Investigação"
        self.key_attribute = Attributes.INT
        self.description = "Você sabe encontrar pistas e informações."
