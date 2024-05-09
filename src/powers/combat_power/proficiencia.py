"""Poder Proficiência"""
from src.powers.base import BasePower


class Proficiencia(BasePower):
    """Representação do poder Proficiência no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Proficiência"
        self.description = "Escolha uma proficiência: armas marciais, armas de fogo, armaduras pesadas ou escudos (se for proficiente em armas marciais, você também pode escolher armas exóticas). Você recebe essa proficiência. Você pode escolher este poder outras vezes para proficiências diferentes."
        self.pre_requisite = {}
