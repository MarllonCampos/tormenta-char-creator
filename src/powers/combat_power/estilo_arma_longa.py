"""Poder Estilo de Arma Longa"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes
from src.skills import Luta


class EstiloArmaLonga(BasePower):
    """Representação do poder Estilo de Arma Longa no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Arma Longa" 
        self.description = "Você recebe +2 em testes de ataque com armas alongadas e pode atacar alvos adjacentes com essas armas. "
        self.pre_requisite = {
          "skills": [Luta()],
          "attributes": {
            Attributes.FOR: 1
          }
        }
