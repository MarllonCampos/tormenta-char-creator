"""Poder Encouraçado"""
from src.powers.base import BasePower
from src.project_typing import Proficiencies


class Encouracado(BasePower):
    """Representação do poder Encouraçado no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Encouraçado"
        self.description = "Se estiver usando uma armadura pesada, você recebe +2 na Defesa. Esse bônus aumenta em +2 para cada outro poder que você possua que tenha Encouraçado como pré-requisito"
        self.pre_requisite = {
          "proficiencies": [Proficiencies.ARMADURA_PESADA]
        }
