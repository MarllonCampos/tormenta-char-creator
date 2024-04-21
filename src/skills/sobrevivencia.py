"""Tamanho Sobrevivência"""
from src.project_typing import Attributes
from .base import BaseSkill


class Sobrevivencia(BaseSkill):
    """Classe que contém as caracteristicas da perícia Sobrevivência"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sobrevivência"
        self.key_attribute = Attributes.SAB
        self.description = "Você está em casa nos ermos."
