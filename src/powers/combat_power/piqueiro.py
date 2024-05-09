"""Poder Piqueiro"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloArmaLonga


class Piqueiro(BasePower):
    """Representação do poder Piqueiro no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Piqueiro"
        self.description = "Uma vez por rodada, se estiver empunhando uma arma alongada e um inimigo entrar voluntariamente em seu alcance corpo a corpo, você pode gastar 1 PM para fazer um ataque corpo a corpo contra este oponente com esta arma. Se o oponente tiver se aproximado fazendo uma investida, seu ataque causa dois dados de dano extra do mesmo tipo."
        self.pre_requisite = {
          "powers":[EstiloArmaLonga()]
        }
