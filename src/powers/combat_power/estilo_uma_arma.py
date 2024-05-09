"""Poder Estilo de Uma Arma"""
from src.powers.base import BasePower
from src.skills import Luta


class EstiloUmaArma(BasePower):
    """Representação do poder Estilo de Uma Arma no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Uma Arma"
        self.description = "Se estiver usando uma arma corpo a corpo em uma das mãos e nada na outra, você recebe +2 na Defesa e nos testes de ataque com essa arma (exceto ataques desarmados)"
        self.pre_requisite = {
          "skills": [Luta()]
        }
