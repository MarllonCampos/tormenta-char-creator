"""Tamanho Intimidação"""
from src.project_typing import Attributes
from .base import BaseSkill


class Intimidacao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Intimidação"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Intimidação"
        self.key_attribute = Attributes.CAR
        self.description = "Você pode assustar ou coagir outras pessoas. Usos de Intimidação são efeitos de medo."
