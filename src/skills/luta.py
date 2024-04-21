"""Tamanho Luta"""
from src.project_typing import Attributes
from .base import BaseSkill


class Luta(BaseSkill):
    """Classe que contém as caracteristicas da perícia Luta"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Luta"
        self.key_attribute = Attributes.FOR
        self.description = "Você usa Luta para fazer ataques corpo a corpo. A CD é a Defesa do alvo. Se você acertar, causa dano de acordo com a arma utilizada."
