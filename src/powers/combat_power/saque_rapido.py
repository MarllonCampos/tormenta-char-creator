"""Poder Saque Rápido"""
from src.powers.base import BasePower
from src.skills import Iniciativa


class SaqueRapido(BasePower):
    """Representação do poder Saque Rápido no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Saque Rápido"
        self.description = "Você recebe +2 em Iniciativa e pode sacar ou guardar itens como uma ação livre (em vez de ação de movimento). Além disso, a ação que você gasta para recarregar armas de disparo diminui em uma categoria (ação completa para padrão, padrão para movimento, movimento para livre)."
        self.pre_requisite = {
          "skills": [Iniciativa()]
        }
