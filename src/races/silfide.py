"""Raça Silfide"""
from src.races import BaseRace
from src.sizes import Medio
from src.project_typing import Attributes

class Silfide(BaseRace):
    def __init__(self):
        super().__init__()
        self.size = Medio()
        self.attributes = [Attributes.CAR, Attributes.CAR, Attributes.DES]
        self.remove_attributes = [Attributes.FOR, Attributes.FOR]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def asas_borboleta(self):
        # TODO -> Seu tamanho é Minúsculo. Você pode 
        # pairar a 1,5m do chão com deslocamento 9m. 
        # Isso permite que você ignore terreno difícil 
        # e o torna imune a dano por queda (a menos que
        # esteja inconsciente). Você pode gastar 1 PM por 
        # rodada para voar com deslocamento de 12m.
        pass

    def espirito_natureza(self):
        # TODO -> Você é uma criatura do tipo espírito,
        # recebe visão na penumbra e pode falar com 
        # animais livremente.
        pass

    def magia_fadas(self):
        # TODO -> Você pode lançar duas das magias 
        # a seguir (atributo chave Carisma): Criar 
        # Ilusão, Enfeitiçar, Luz (como uma magia 
        # arcana) e Sono. Caso aprenda novamente 
        # uma dessas magias, seu custo diminui em –1 PM
        pass
