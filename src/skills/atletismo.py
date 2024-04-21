"""Tamanho Atletismo"""
from src.project_typing import Attributes
from .base import BaseSkill


class Atletismo(BaseSkill):
    """Classe que contém as caracteristicas da perícia Atletismo"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Atletismo"
        self.key_attribute = Attributes.FOR
        self.description = "Você pode realizar façanhas atléticas."
