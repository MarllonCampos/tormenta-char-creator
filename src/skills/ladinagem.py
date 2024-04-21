"""Tamanho Ladinagem"""
from src.project_typing import Attributes
from .base import BaseSkill


class Ladinagem(BaseSkill):
    """Classe que contém as caracteristicas da perícia Ladinagem"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ladinagem"
        self.key_attribute = Attributes.DES
        self.only_trained = True
        self.armor_penalty = True
        self.description = "Você sabe exercer atividades ilícitas."
