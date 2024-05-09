"""Poder Carga de Cavalaria"""
from src.powers.base import BasePower
from src.powers.combat_power import Ginete


class CargaCavalaria(BasePower):
    """Representação do poder Carga de Cavalaria no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Carga de Cavalaria"
        self.description = "Quando faz uma investida montada, você causa +2d8 pontos de dano. Além disso, pode continuar se movendo depois do ataque. Você deve se mover em linha reta e seu movimento máximo ainda é o dobro do seu deslocamento."
        self.pre_requisite = {
          "skills": [Ginete()]
        }
