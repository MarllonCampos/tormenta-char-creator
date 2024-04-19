"""Golem"""
from src.races.base import BaseRace

from src.project_typing import Attributes


class Golem(BaseRace):
    """Descritivo das caracteristicas da Raça Golem"""
    def __init__(self):

        self.size = Medio()
        self.attributes = [Attributes.FOR, Attributes.FOR, Attributes.CON]
        self.remove_attributes = [Attributes.CAR]
        self.except_attributes = None
        self.any_attribute = None
        print(__class__.__name__)

    def chassi(self):
        # TODO -> Seu corpo artificial é resistente, mas rígido.
        # Seu deslocamento é 6m, mas não é reduzido por uso de
        # armadura ou excesso de carga.
        # Você recebe +2 na Defesa, mas possui penalidade de armadura –2.
        # Você leva um dia para vestir ou removeruma armadura
        # (pois precisa acoplar as peças dela a seu chassi).
        # Por ser acoplada, sua armadura não conta no limite de itens que
        # você pode usar (mas você continua só podendo usar uma armadura).
        pass

    def criatura_artificial(self):
        # TODO -> Você é uma criatura do tipo construto.
        # Recebe visão no escuro e imunidade a efeitos de cansaço,
        # metabólicos e de veneno.
        # Além disso, não precisa respirar, alimentar-se ou dormir,
        # mas não se beneficia de cura mundana e de itens
        # da categoria alimentação.
        # Você precisa ficar inerte por oito horas por dia para recarregar sua
        # fonte de energia. Se fizer isso, recupera PV e PM por descanso
        # em condições normais (golens não são afetados por condições boas
        # ou ruins de descanso). Por fim, a perícia Cura não funciona em você,
        # mas Ofício (artesão) pode ser usada no lugar dela.
        pass

    def fonte_elemental(self):
        # TODO -> Você possui um espírito elemental preso em seu corpo.
        # Escolha entre água (frio), ar (eletricidade), fogo (fogo)
        # e terra (ácido).
        # Você é imune a dano desse tipo. Se fosse sofrer dano
        # mágico desse tipo,
        # em vez disso cura PV em quantidade igual à metade do dano.
        # Por exemplo, se um golem com espírito elemental do fogo é atingido
        # por uma Bola de Fogo que causa 30 pontos de dano,
        # em vez de sofrer esse dano, ele recupera 15 PV.
        pass

    def proposito_criacao(self):
        # TODO -> Você foi construído “pronto” para um
        # propósito específico e não teve uma infância.
        # Você não tem direito a escolher uma origem, mas recebe um
        # poder geral a sua escolha.
        pass
