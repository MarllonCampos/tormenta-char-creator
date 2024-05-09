"""Poder Arremesso Potente"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloArremesso
from src.project_typing.attributes import Attributes


class ArremessoPotente(BasePower):
    """Representação do poder Arremesso Potente no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Arremesso Potente"
        self.description = "Quando usa uma arma de arremesso, você pode usar sua Força em vez de Destreza nos testes de ataque. Se você possuir o poder Ataque Poderoso, poderá usá-lo com armas de arremesso."
        self.pre_requisite = {
          "attributes": {
            Attributes.FOR: 1,
          },
          "powers": [EstiloArremesso()]
        }
