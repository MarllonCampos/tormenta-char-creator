"""Marreta"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Marreta(BaseWeapon):
    """Representação da Marreta no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Marreta"
        self.price = 20
        self.damage = "3d4"
        self.weapon_threat = "x2"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.IMPACTO
        self.weight = 2
