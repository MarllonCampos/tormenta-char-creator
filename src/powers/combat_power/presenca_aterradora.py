"""Poder Presença Aterradora"""
from src.powers.base import BasePower
from src.skills import Intimidacao


class PresencaAterradora(BasePower):
    """Representação do poder Presença Aterradora no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Presença Aterradora"
        self.description = "Você pode gastar uma ação padrão e 1 PM para assustar todas as criaturas a sua escolha em alcance curto. Veja a perícia Intimidação para as regras de assustar."
        self.pre_requisite = {
          "skills": [Intimidacao()]
        }
