"""Poder Reflexos de Combate"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes


class ReflexosCombate(BasePower):
    """Representação do poder Reflexos de Combate no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Reflexos de Combate"
        self.description = "Você ganha uma ação de movimento extra no seu primeiro turno de cada combate."
        self.pre_requisite = {
          "attributes": {
            Attributes.DES: 1,
          }
        }
