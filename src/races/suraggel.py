"""Suraggel Raça Base para Aggelus e Sulfure"""
from src.races.base import BaseRace



class Suraggel(BaseRace):
    """Raça base para outras duas raças [Aggelus | Sulfure]"""
    def __init__(self):
        super().__init__()
        self.attributes = None
        self.remove_attributes = None
        self.except_attributes = None
        self.any_attribute = None
        


    def heranca_divina(self):
        # TODO -> Você é uma criatura do tipo espírito
        # e recebe visão no escuro.
        pass
