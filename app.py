from src.weapons.store import StoreWeapons
from src.project_typing import WeaponHilt, WeaponProficiency, WeaponRange
store = StoreWeapons()

weaponHilt = [WeaponHilt.LEVE, WeaponProficiency.MARCIAL, WeaponRange.MEDIO]
store.showcase(weapon_attributes=weaponHilt)
