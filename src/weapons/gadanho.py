"""Gadanho"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Gadanho(BaseWeapon):
    """Representação da Gadanho no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Gadanho"
        self.price = 18
        self.damage = "2d4"
        self.weapon_threat = "x4"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 2
