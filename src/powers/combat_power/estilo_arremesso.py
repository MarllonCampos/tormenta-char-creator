"""Poder Estilo de Arremesso"""
from src.powers.base import BasePower
from src.skills import Pontaria


class EstiloArremesso(BasePower):
    """Representação do poder Estilo de Arremesso no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Estilo de Arremesso"
        self.description = "Você pode sacar armas de arremesso como uma ação livre e recebe +2 nas rolagens de dano com elas. Se também possuir o poder Saque Rápido, também recebe +2 nos testes de ataque com essas armas"
        self.pre_requisite = {
          "skills": [Pontaria()]
        }
