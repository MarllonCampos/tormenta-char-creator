"""Besta Pesada"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class BestaPesada(BaseWeapon):
    """Representação da Besta Pesada no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = False
        self.hilt = WeaponHilt.DUPLA
        self.name = "Besta Pesada"
        self.price = 50
        self.damage = "1d12"
        self.weapon_threat = 19
        self.range = WeaponRange.MEDIO
        self.type =  WeaponType.PERFURACAO
        self.weight = 2
        # TODO -> Criar uma classe de Virotes que extende ammunition
        # self.ammunition = "Virotes"
