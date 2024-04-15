"""Espada Bastarda"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class EspadaBastarda(BaseWeapon):
    """Representação da Espada Bastarda no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Espada Bastarda"
        self.price = 35
        self.damage = ["1d10", "1d12"]
        self.weapon_threat = 19
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 1
