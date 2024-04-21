"""Tamanho Religião"""
from src.project_typing import Attributes
from .base import BaseSkill


class Religiao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Religião"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Religião"
        self.key_attribute = Attributes.SAB
        self.only_trained = True
        self.description = "Você possui conhecimento sobre os deuses e as religiões de Arton"
