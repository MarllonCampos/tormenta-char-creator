"""Poder Estilo de Arma e Escudo"""
from src.powers.base import BasePower
from src.project_typing import Proficiencies
from src.skills import Luta


class EstiloArmaEscudo(BasePower):
    """Representação do poder Estilo de Arma e Escudo no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Arma e Escudo"
        self.description = "Se você estiver usando um escudo, o bônus na Defesa que ele fornece aumenta em +2."
        self.pre_requisite = {
          "skills": [Luta()],
          "proficiencies": [Proficiencies.ESCUDO]
        }
