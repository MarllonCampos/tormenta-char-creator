"""Poder Trespassar"""
from src.powers.base import BasePower
from src.powers.combat_power import AtaquePoderoso


class Trespassar(BasePower):
    """Representação do poder Trespassar no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Trespassar"
        self.description = "Quando você faz um ataque corpo a corpo e reduz os pontos de vida do alvo para 0 ou menos, pode gastar 1 PM para fazer um ataque adicional contra outra criatura dentro do seu alcance."
        self.pre_requisite = {
          "powers": [AtaquePoderoso()]
        }
