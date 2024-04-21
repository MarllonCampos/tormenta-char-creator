"""Tamanho Fortitude"""
from src.project_typing import Attributes
from .base import BaseSkill


class Fortitude(BaseSkill):
    """Classe que contém as caracteristicas da perícia Fortitude"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Fortitude"
        self.key_attribute = Attributes.CON
        self.description = "Você usa esta perícia para resistir a efeitos que exigem vitalidade, como doenças e venenos. A CD é determinada pelo efeito. Você também usa Fortitude para manter seu fôlego quando está correndo ou sem respirar. A CD é 15 +1 por teste anterior."
