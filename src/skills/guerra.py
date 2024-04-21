"""Tamanho Guerra"""
from src.project_typing import Attributes
from .base import BaseSkill


class Guerra(BaseSkill):
    """Classe que contém as caracteristicas da perícia Guerra"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Guerra"
        self.key_attribute = Attributes.INT
        self.only_trained = True
        self.description = "Você foi educado em tática, estratégia e logística."
