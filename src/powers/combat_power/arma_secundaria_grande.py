"""Poder Arma Secundária Grande"""
from src.powers.base import BasePower
from src.powers.combat_power.estilo_duas_armas import EstiloDuasArmas
from src.project_typing.attributes import Attributes
from src.skills import Luta


class ArmaSecundariaGrande(BasePower):
    """Representação do poder Arma Secundária Grande no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Arma Secundária Grande"
        self.description = "Se estiver empunhando duas armas (e pelo menos uma delas for leve) e fizer a ação agredir, você pode fazer dois ataques, um com cada arma. Se fizer isso, sofre –2 em todos os testes de ataque até o seu próximo turno. Se possuir Ambidestria, em vez disso não sofre penalidade para usá-lo"
        self.pre_requisite = {
          "skills": [Luta()],
          "attributes": {
            Attributes.DES: 2
          },
          "powers": [EstiloDuasArmas()]
        }
