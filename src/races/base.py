"""Classe Base para raças"""
from typing import List

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
