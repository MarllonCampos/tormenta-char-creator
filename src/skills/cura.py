"""Tamanho Cura"""
from src.project_typing import Attributes
from .base import BaseSkill


class Cura(BaseSkill):
    """Classe que contém as caracteristicas da perícia Cura"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cura"
        self.key_attribute = Attributes.SAB
        self.description = "Você sabe tratar ferimentos, doenças e venenos."
