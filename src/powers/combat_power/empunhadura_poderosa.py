"""Poder Empunhadura Poderosa"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes


class EmpunhaduraPoderosa(BasePower):
    """Representação do poder Empunhadura Poderosa no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Empunhadura Poderosa"
        self.description = "Ao usar uma arma feita para uma categoria de tamanho maior que a sua, a penalidade que você sofre nos testes de  ataque diminui para –2 (normalmente, usar uma arma de uma categoria de tamanho maior impõe –5 nos testes de ataque)."
        self.pre_requisite = {
          "attributes": {
            Attributes.FOR: 3,
          }
        }
