"""Tamanho Atuação"""
from src.project_typing import Attributes
from .base import BaseSkill


class Atuacao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Atuação"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Atuação"
        self.key_attribute = Attributes.CAR
        self.only_trained = True
        self.description = "Você sabe fazer apresentações artística incluindo música, dança e dramaturgia."
