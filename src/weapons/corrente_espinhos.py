"""Corrente de Espinhos"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class CorrenteEspinhos(BaseWeapon):
    """Representação da Corrente de Espinhos no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Corrente de Espinhos"
        self.price = 25
        self.damage = ["2d4","2d4"]
        self.weapon_threat = 19
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 2
