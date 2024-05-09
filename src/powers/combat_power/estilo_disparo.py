"""Poder Estilo de Disparo"""
from src.powers.base import BasePower
from src.skills import Pontaria


class EstiloDisparo(BasePower):
    """Representação do poder Estilo de Disparo no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Disparo"
        self.description = "Se estiver usando uma arma de disparo, você soma sua Destreza nas rolagens de dano."
        self.pre_requisite = {
          "skills": [Pontaria()]
        }
