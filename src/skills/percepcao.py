"""Tamanho Percepção"""
from src.project_typing import Attributes
from .base import BaseSkill


class Percepcao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Percepção"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Percepção"
        self.key_attribute = Attributes.SAB
        self.description = "Você nota coisas usando seus sentidos."
