"""Pistola"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Pistola(BaseWeapon):
    """Representação da Pistola no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = False
        self.hilt = WeaponHilt.LEVE
        self.name = "Pistola"
        self.price = 250
        self.damage = "2d6"
        self.weapon_threat = [19,"x3"]
        self.range = WeaponRange.CURTO
        self.type =  WeaponType.PERFURACAO
        self.weight = 1
