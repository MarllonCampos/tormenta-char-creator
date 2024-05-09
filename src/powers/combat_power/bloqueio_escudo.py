"""Poder Bloqueio com Escudo"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloArmaEscudo


class BloqueioEscudo(BasePower):
    """Representação do poder Bloqueio com Escudo no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bloqueio com Escudo"
        self.description = "Quando sofre dano, você pode gastar 1 PM para receber redução de dano igual ao bônus na Defesa que seu escudo fornece contra este dano. Você só pode usar este poder se estiver usando um escudo."
        self.pre_requisite = {
            "powers": [EstiloArmaEscudo()]
        }
