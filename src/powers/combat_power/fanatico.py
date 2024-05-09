"""Poder Fanático"""
from src.powers.base import BasePower
from src.powers.combat_power import Encouracado


class Fanatico(BasePower):
    """Representação do poder Fanático no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Fanático"
        self.description = "Seu deslocamento não é reduzido por usar armaduras pesadas."
        self.pre_requisite = {
          "powers": [Encouracado()]
        }
