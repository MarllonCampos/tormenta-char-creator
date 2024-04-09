from typing import List
from src.project_typing import WeaponHilt, WeaponProficiency, WeaponRange, WeaponType
from src.weapons import ALL_WEAPONS
from src.weapons.base import BaseWeapon

class StoreWeapons:
    """Uma classe padrão para poder mostrar as armas que existem e seus preços"""

    def showcase(weapon_hilt: WeaponHilt | List[WeaponHilt] = None ) -> List[BaseWeapon]:
        """Função que mostra todas as armas possíveis podendo ser filtradas """
        weapon_hilt_formatted_array =  []

        if weapon_hilt is None: 
            return ALL_WEAPONS
        if isinstance(weapon_hilt, list) or isinstance(weapon_hilt, List) :
            weapon_hilt_formatted_array = weapon_hilt
        else:
            weapon_hilt_formatted_array = [weapon_hilt]

        text = ""
        for weapon in ALL_WEAPONS:
            if weapon_hilt is not None and (weapon.hilt not in weapon_hilt_formatted_array):
                continue
            text += f"{weapon.name}\n"
        print(text)
