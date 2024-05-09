"""Poder Derrubar Aprimorado"""
from src.powers.base import BasePower
from src.powers.combat_power import CombateDefensivo


class DerrubarAprimorado(BasePower):
    """Representação do poder Derrubar Aprimorado no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Derrubar Aprimorado"
        self.description = "Você recebe +2 em testes de ataque para derrubar. Quando derruba uma criatura com essa manobra, pode gastar 1 PM para fazer um ataque extra contra ela."
        self.pre_requisite = {
          "powers": [CombateDefensivo()]
        }
