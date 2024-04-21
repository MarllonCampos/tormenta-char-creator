"""Tamanho Pontaria"""
from src.project_typing import Attributes
from .base import BaseSkill


class Pontaria(BaseSkill):
    """Classe que contém as caracteristicas da perícia Pontaria"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pontaria"
        self.key_attribute = Attributes.DES
        self.description = "Você usa Pontaria para fazer ataques à distância. A CD é a Defesa do alvo. Se você acertar, causa dano de acordo com a arma utilizada"
