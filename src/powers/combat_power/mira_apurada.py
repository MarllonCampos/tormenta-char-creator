"""Poder Disparo Preciso"""
from src.powers.base import BasePower
from src.powers.combat_power import DisparoPreciso
from src.project_typing.attributes import Attributes


class MiraApurada(BasePower):
    """Representação do poder Disparo Preciso no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Mira Apurada"
        self.description = "Quando usa a ação mirar, você recebe +2 em testes de ataque e na margem de ameaça com ataques à distância até o fim do turno."
        self.pre_requisite = {
          "powers": [DisparoPreciso()],
          "attributes": {
              Attributes.SAB: 1
          }
        }
