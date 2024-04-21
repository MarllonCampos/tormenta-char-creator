"""Tamanho Intuição"""
from src.project_typing import Attributes
from .base import BaseSkill


class Intuicao(BaseSkill):
    """Classe que contém as caracteristicas da perícia Intuição"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Intuição"
        self.key_attribute = Attributes.SAB
        self.description = "Esta perícia mede sua empatia e “sexto sentido”."
