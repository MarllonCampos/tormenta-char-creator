"""Poder Ataque com Escudo"""
from src.powers.base import BasePower
from src.powers.combat_power import EstiloArmaEscudo


class AtaqueEscudo(BasePower):
    """Representação do poder Ataque com Escudo no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ataque com Escudo"
        self.description = "Quando faz um ataque corpo a corpo com uma arma de duas mãos, você pode pagar 1 PM. Se fizer isso e acertar o ataque, além do dano você faz uma manobra derrubar ou empurrar contra o alvo como uma ação livre (use o resultado do ataque como o teste de manobra)."
        self.pre_requisite = {
            "powers": [EstiloArmaEscudo()]
        }
