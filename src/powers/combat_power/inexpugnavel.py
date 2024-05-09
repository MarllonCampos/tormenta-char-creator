"""Poder Inexpugnável"""
from src.powers.base import BasePower
from src.powers.combat_power import Encouracado


class Inexpugnavel(BasePower):
    """Representação do poder Inexpugnável no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Inexpugnável"
        self.description = "Se estiver usando uma armadura pesada, você recebe +2 em todos os testes de resistência."
        self.pre_requisite = {
          "powers": [Encouracado()]
        }
