"""Poder Ginete"""
from src.powers.base import BasePower
from src.skills import Cavalgar


class Ginete(BasePower):
    """Representação do poder Ginete no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ginete"
        self.description = "Você passa automaticamente em testes de Cavalgar para não cair da montaria quando sofre dano. Além disso, não sofre penalidades para atacar à distância ou lançar magias quando montado."
        self.pre_requisite = {
          "skills": [Cavalgar()]
        }
