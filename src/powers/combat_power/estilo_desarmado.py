"""Poder Estilo Desarmado"""
from src.powers.base import BasePower
from src.skills import Luta


class EstiloDesarmado(BasePower):
    """Representação do poder Estilo Desarmado no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo Desarmado"
        self.description = "Seus ataques desarmados causam 1d6 pontos de dano e podem causar dano letal ou não letal (sem penalidades)."
        self.pre_requisite = {
          "skills": [Luta()]
        }
