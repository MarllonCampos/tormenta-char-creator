"""Poder Quebrar Aprimorado"""
from src.powers.base import BasePower
from src.powers.combat_power import AtaquePoderoso


class QuebrarAprimorado(BasePower):
    """Representação do poder Quebrar Aprimorado no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Quebrar Aprimorado"
        self.description = "Você recebe +2 em testes de ataque para quebrar. Quando reduz os PV de uma arma para 0 ou menos, você pode gastar 1 PM para realizar um ataque extra contra o usuário dela. O ataque adicional usa os mesmos valores de ataque e dano, mas os dados devem ser rolados novamente."
        self.pre_requisite = {
          "powers": [AtaquePoderoso()]
        }
