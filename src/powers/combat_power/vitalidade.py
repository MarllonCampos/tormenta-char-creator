"""Poder Vitalidade"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes


class Vitalidade(BasePower):
    """Representação do poder Vitalidade no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Vitalidade"
        self.description = "Você recebe +1 PV por nível de personagem e +2 em Fortitude."
        self.pre_requisite = {
          "attributes": {
            Attributes.CON: 1,
          }
        }
