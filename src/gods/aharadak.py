"""Classe que descreve o deus Aharadak"""
from src.races.base import BaseRace
from src.project_typing import EnergiesEnum
from src.weapons import CorrenteEspinhos
from .base import BaseGod


class Aharadak(BaseGod):
    """Descritivo das caracteristicas do Deus Aharadak"""

    def __init__(self) -> None:
        super().__init__()
        self.name = __class__.__name__
        self.blessed_weapons = CorrenteEspinhos()
        self.energy = EnergiesEnum.NEGATIVA
        self.provided_powers = []
        self.beliefs: str = "Reverenciar a Tormenta, pregar a inevitabilidade de sua chegada ao mundo. Praticar a devassidão e a perversão. Deturpar tudo que é correto, desfigurar tudo que é normal. Abraçar a agonia, crueldade e loucura"
        self.followers: BaseRace  = [BaseRace]
        self.obligations_restrictions: str = "Quase todos os cultistas de Aharadak são maníacos insanos, compelidos a praticar os atos mais abomináveis. No entanto, talvez devido à natureza alienígena e incompreensível deste deus, alguns devotos conseguem se resguardar. Preservam sua humanidade, abstendo-se de cometer crimes ou profanações. Ainda assim, o devoto paga um preço. No início de qualquer cena de ação, role 1d6. Com um resultado ímpar, você fica fascinado na primeira rodada, perdido em devaneios sobre a futilidade da vida (mesmo que seja imune a esta condição)"
