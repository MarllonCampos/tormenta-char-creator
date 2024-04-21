"""Tamanho Enganação"""
from src.project_typing import Attributes
from .base import BaseSkill


class Enganacao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Enganação"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Enganação"
        self.key_attribute = Attributes.CAR
        self.description = "Você manipula pessoas com blefes e trapaças."
