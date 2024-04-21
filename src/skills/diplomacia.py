"""Tamanho Diplomacia"""
from src.project_typing import Attributes
from .base import BaseSkill


class Diplomacia(BaseSkill):
    """Classe que contém as caracteristicas da perícia Diplomacia"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Diplomacia"
        self.key_attribute = Attributes.CAR
        self.description = "Você convence pessoas com lábia e argumentação.Usos de Diplomacia são efeitos mentais."
