"""Poder Esquiva"""
from src.powers.base import BasePower
from src.project_typing import Attributes


class Esquiva(BasePower):
    """Representação do poder Esquiva no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Esquiva"
        self.description = "Você recebe +2 na Defesa e Reflexos."
        self.pre_requisite = {
          "attributes": {
            Attributes.DES: 1,
          }
        }
