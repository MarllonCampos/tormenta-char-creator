"""Tamanho Pilotagem"""
from src.project_typing import Attributes
from .base import BaseSkill


class Pilotagem(BaseSkill):
    """Classe que contém as caracteristicas da perícia Pilotagem"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pilotagem"
        self.key_attribute = Attributes.DES
        self.only_trained = True
        self.description = "Você sabe operar veículos como carroças, barcos e balões. Ações simples não exigem testes"
