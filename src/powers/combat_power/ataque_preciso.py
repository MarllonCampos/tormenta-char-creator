"""Poder Ataque Preciso"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloUmaArma


class AtaquePreciso(BasePower):
    """Representação do poder Ataque Preciso no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ataque Preciso"
        self.description = "Se estiver empunhando uma arma corpo a corpo em uma das mãos e nada na outra, você recebe +2 na margem de ameaça e +1 no multiplicador de crítico."
        self.pre_requisite = {
            "powers": [EstiloUmaArma()]
        }
