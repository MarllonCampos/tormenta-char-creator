"""Chicote"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Chicote(BaseWeapon):
    """Representação da Chicote no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Chicote"
        self.price = 2
        self.damage = "1d3"
        self.weapon_threat = "x2"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 1
