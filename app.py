"""Entrada central para todas as aplicações"""
from src.weapons.store import StoreWeapons
from src.project_typing import WeaponHilt, WeaponProficiency, WeaponRange
from src.races import Osteon
store = StoreWeapons()

weaponHilt = [WeaponProficiency.EXOTICA]



# store.showcase()


Osteon()