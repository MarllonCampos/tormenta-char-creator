"""Poder Acuidade com Arma"""
from src.powers.base import BasePower
from src.project_typing.attributes import Attributes


class AcuidadeArma(BasePower):
    """Representação do poder Acuidade com Arma no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Acuidade com Arma"
        self.description = "Quando usa uma arma corpo a corpo leve ou uma arma de arremesso, você pode usar sua Destreza em vez de Força nos testes de ataque e rolagens de dano"
        self.pre_requisite = {
          "attributes": {
            Attributes.DES: 1,
          }
        }
        print(self.name)
