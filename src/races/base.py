"""Classe Base para raças"""
from typing import List
from src.sizes import Medio
from src.project_typing import Attributes
from src.sizes import BaseSize, Medio


class BaseRace():
    """Uma classe padrão para extender para as próximas raças."""
    def __init__(self):
        self.increase_attribute: List[Attributes] | None = None
        self.reduce_attributes: List[Attributes] | None = None
        self.cant_choose_attributes: List[Attributes] | None = None
        self.any_attribute: int | None = None
        self.size: BaseSize = Medio()

    def all_methods(self):
        current_method_name = "all_methods"
        return [attribute for attribute in dir(self) if callable(getattr(self, attribute)) and not attribute.startswith("__") and attribute is not current_method_name]
        