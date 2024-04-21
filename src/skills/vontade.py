"""Tamanho Vontade"""
from src.project_typing import Attributes
from .base import BaseSkill


class Vontade(BaseSkill):
    """Classe que contém as caracteristicas da perícia Vontade"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Vontade"
        self.key_attribute = Attributes.SAB
        self.description = "Você usa esta perícia para resistir a efeitos que exigem determinação, como intimidação e encantamentos. A CD é determinada pelo efeito. Testes de Vontade são testes de resistência."
