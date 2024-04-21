"""Tamanho Nobreza"""
from src.project_typing import Attributes
from .base import BaseSkill


class Nobreza(BaseSkill):
    """Classe que contém as caracteristicas da perícia Nobreza"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Nobreza"
        self.key_attribute = Attributes.INT
        self.only_trained = True
        self.description = "Você recebeu a educação de um nobre."
