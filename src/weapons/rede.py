"""Rede"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponRange, WeaponProficiency, WeaponHilt
class Rede(BaseWeapon):
    """Representação da Rede no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Rede"
        self.price = 20
        self.damage = None
        self.weapon_threat = None
        self.range = WeaponRange.CURTO
        self.type =  None
        self.weight = 1
