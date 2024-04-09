"""Alfange"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Alfange(BaseWeapon):
    """Representação da Alfange no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Alfange"
        self.price = 75
        self.damage = "2d4"
        self.weapon_threat = 18
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 2
