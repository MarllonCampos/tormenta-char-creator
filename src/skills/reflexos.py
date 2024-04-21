"""Tamanho Reflexos"""
from src.project_typing import Attributes
from .base import BaseSkill


class Reflexos(BaseSkill):
    """Classe que contém as caracteristicas da perícia Reflexos"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Reflexos"
        self.key_attribute = Attributes.DES
        self.description = "Você usa esta perícia para resistir a efeitos que exigem reação rápida, como armadilhas e explosões. A CD é determinada pelo efeito. Você também usa Reflexos para evitar fintas."
