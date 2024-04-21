"""Tamanho Misticismo"""
from src.project_typing import Attributes
from .base import BaseSkill


class Misticismo(BaseSkill):
    """Classe que contém as caracteristicas da perícia Misticismo"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Misticismo"
        self.key_attribute = Attributes.INT
        self.only_trained = True
        self.description = "Esta perícia envolve o conhecimento de magias, itens mágicos e fenômenos sobrenaturais."
