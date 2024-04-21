"""Tamanho Cavalgar"""
from src.project_typing import Attributes
from .base import BaseSkill


class Cavalgar(BaseSkill):
    """Classe que contém as caracteristicas da perícia Cavalgar"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cavalgar"
        self.key_attribute = Attributes.DES
        self.description = "Você sabe conduzir animais de montaria, como cavalos, trobos e grifos. Ações simples não exigem testes — você pode encilhar, montar, cavalgar em terreno plano e desmontar automaticamente. Ações perigosas, entretanto, exigem testes da perícia"
