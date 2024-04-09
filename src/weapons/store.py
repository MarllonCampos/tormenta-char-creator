from typing import List, Union
from src.project_typing import WeaponHilt, WeaponProficiency, WeaponRange, WeaponType
from src.weapons import ALL_WEAPONS
from src.weapons.base import BaseWeapon

class StoreWeapons:
    """Uma classe padrão para poder mostrar as armas que existem e seus preços"""
    weapon_hilt_union =  Union[WeaponHilt, List[WeaponHilt]]
    weapon_proficiency_union = Union[WeaponProficiency, List[WeaponProficiency]]
    weapon_range_union = Union[WeaponRange, List[WeaponRange]]
    weapon_type_union = Union[WeaponType, List[WeaponType]]
    WeaponAttributesUnion = Union[weapon_hilt_union,weapon_proficiency_union,
                                    weapon_range_union, weapon_type_union]

    @staticmethod
    def showcase(weapon_attributes: WeaponAttributesUnion = None ) -> List[BaseWeapon]:
        """Função que mostra todas as armas possíveis podendo ser filtradas """
        weapon_hilt_formatted_array =  []

        print(weapon_attributes)
