"""Machado Taurico"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class MachadoTaurico(BaseWeapon):
    """Representação da Machado Taurico no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.EXOTICA
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Machado Taurico"
        self.price = 50
        self.damage = "2d8"
        self.weapon_threat = "x3"
        self.range = WeaponRange.PESSOAL
        self.type =  WeaponType.CORTE
        self.weight = 2
