"""Tacape"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Tacape(BaseWeapon):
    """Representação da Tacape no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.IMPACTO
        self.weight = 2
        self.damage = "1d10"
        self.range = WeaponRange.PESSOAL
        self.weapon_threat = "x2"
        self.price = None
        self.name = "Tacape"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
