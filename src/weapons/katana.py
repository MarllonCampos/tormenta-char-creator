"""Katana"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Katana(BaseWeapon):
    """Representação da Katana no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Katana"
        self.price = 100
        self.damage = ["1d8","1d10"]
        self.weapon_threat = 19
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 1
