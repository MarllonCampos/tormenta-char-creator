"""Poder Disparo Preciso"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloDisparo


class DisparoPreciso(BasePower):
    """Representação do poder Disparo Preciso no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Disparo Preciso"
        self.description = "Você pode fazer ataques à distância contra oponentes envolvidos em combate corpo a corpo sem sofrer a penalidade de –5 no teste de ataque."
        self.pre_requisite = {
          # TODO -> Criar um OR para permitir mais de um requisito por poder
          "powers": [EstiloDisparo()] 
        }
