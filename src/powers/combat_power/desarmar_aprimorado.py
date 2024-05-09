"""Poder Desarmar Aprimorado"""
from src.powers.base import BasePower
from src.powers.combat_power import CombateDefensivo


class DesarmarAprimorado(BasePower):
    """Representação do poder Desarmar Aprimorado no Tormenta20"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Desarmar Aprimorado"
        self.description = "Você recebe +2 em testes de ataque para desarmar. Quando desarma uma criatura, pode gastar 1 PM para arremessar a arma dela para longe. Para definir onde a arma cai, role 1d8 para a direção (sendo “1” diretamente à sua frente, “2” à frente e à direita e assim por diante) e 1d6 para a distância (medida em quadrados de 1,5m a partir da criatura desarmada)."
        self.pre_requisite = {
          "powers": [CombateDefensivo()]
        }
