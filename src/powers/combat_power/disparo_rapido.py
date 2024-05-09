"""Poder Disparo Rápido"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloDisparo
from src.project_typing.attributes import Attributes


class DisparoRapido(BasePower):
    """Representação do poder Disparo Rápido no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Disparo Rápido"
        self.description = "Se estiver empunhando uma arma de disparo que possa recarregar como ação livre e gastar uma ação completa para agredir, pode fazer um ataque adicional com ela. Se fizer isso, sofre –2 em todos os testes de ataque até o seu próximo turno."
        self.pre_requisite = {
          "powers": [EstiloDisparo()],
          "attributes": {
              Attributes.DES: 1
          }
        }
