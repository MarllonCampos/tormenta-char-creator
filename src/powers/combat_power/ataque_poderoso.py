"""Poder Ataque Poderoso"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes


class AtaquePoderoso(BasePower):
    """Representação do poder Ataque Poderoso no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ataque Poderoso"
        self.description = "Sempre que faz um ataque corpo a corpo, você pode sofrer –2 no teste de ataque para receber +5 na rolagem de dano."
        self.pre_requisite = {
          "attributes": {
            Attributes.FOR: 1,
          }
        }
