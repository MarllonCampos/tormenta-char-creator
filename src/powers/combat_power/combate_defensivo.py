"""Poder Combate Defensivo"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes


class CombateDefensivo(BasePower):
    """Representação do poder Combate Defensivo no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Combate Defensivo"
        self.description = "Quando usa a ação agredir, você pode usar este poder. Se fizer isso, até seu próximo turno, sofre –2 em todos os testes de ataque, mas recebe +5 na Defesa."
        self.pre_requisite = {
          "attributes": {
            Attributes.INT: 1,
          }
        }
