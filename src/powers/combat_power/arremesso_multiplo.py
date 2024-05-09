"""Poder Arremesso Múltiplo"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloArremesso
from src.project_typing.attributes import Attributes


class ArremessoMultiplo(BasePower):
    """Representação do poder Arremesso Múltiplo no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Arremesso Múltiplo"
        self.description = "Uma vez por rodada, quando faz um ataque com uma arma de arremesso, você pode gastar 1 PM para fazer um ataque adicional contra o mesmo alvo, arremessando outra arma de arremesso."
        self.pre_requisite = {
          "attributes": {
            Attributes.DES: 1,
          },
          "powers": [EstiloArremesso()]
        }
