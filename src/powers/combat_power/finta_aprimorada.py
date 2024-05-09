"""Poder Finta Aprimorada"""
from src.powers.base import BasePower
from src.skills import Enganacao


class FintaAprimorada(BasePower):
    """Representação do poder Finta Aprimorada no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Finta Aprimorada"
        self.description = "Você recebe +2 em testes de Enganação para fintar e pode fintar como uma ação de movimento."
        self.pre_requisite = {
          "skills": [Enganacao()]
        }
