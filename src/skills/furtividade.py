"""Tamanho Furtividade"""
from src.project_typing import Attributes
from .base import BaseSkill


class Furtividade(BaseSkill):
    """Classe que contém as caracteristicas da perícia Furtividade"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Furtividade"
        self.key_attribute = Attributes.DES
        self.armor_penalty = True
        self.description = "Você usa esta perícia para resistir a efeitos que exigem vitalidade, como doenças e venenos. A CD é determinada pelo efeito. Você também usa Furtividade para manter seu fôlego quando está correndo ou sem respirar. A CD é 15 +1 por teste anterior."
