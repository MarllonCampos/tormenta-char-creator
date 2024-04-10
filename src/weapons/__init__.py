"""Arquivo usado para exportar as classes das armas"""
from typing import List
from .adaga import Adaga
from .alabarda import Alabarda
from .alfange import Alfange
from .arco_curto import ArcoCurto
from .arco_longo import ArcoLongo
from .azagaia import Azagaia
from .besta_leve import BestaLeve
from .besta_pesada import BestaPesada
from .bordao import Bordao
from .chicote import Chicote
from .cimitarra import Cimitarra
from .clava import Clava
from .corrente_espinhos import CorrenteEspinhos
from .espada_bastarda import EspadaBastarda
from .espada_curta import EspadaCurta
from .espada_longa import EspadaLonga
from .florete import Florete
from .foice import Foice
from .gadanho import Gadanho
from .katana import Katana
from .lanca import Lanca
from .lanca_montada import LancaMontada
from .maca import Maca
from .machadinha import Machadinha
from .machado_anao import MachadoAnao
from .machado_batalha import MachadoBatalha
from .machado_guerra import MachadoGuerra
from .machado_taurico import MachadoTaurico
from .mangual import Mangual
from .marreta import Marreta
from .martelo_guerra import MarteloGuerra
from .montante import Montante
from .mosquete import Mosquete
from .picareta import Picareta
from .pique import Pique
from .pistola import Pistola
from .rede import Rede
from .tacape import Tacape
from .tridente import Tridente
from .base import BaseWeapon


ALL_WEAPONS: List[BaseWeapon] = [Adaga(),
Alabarda(),
Alfange(),
ArcoCurto(),
ArcoLongo(),
Azagaia(),
BestaLeve(),
BestaPesada(),
Bordao(),
Chicote(),
Cimitarra(),
Clava(),
CorrenteEspinhos(),
EspadaBastarda(),
EspadaCurta(),
EspadaLonga(),
Florete(),
Foice(),
Gadanho(),
Katana(),
Lanca(),
LancaMontada(),
Maca(),
Machadinha(),
MachadoAnao(),
MachadoBatalha(),
MachadoGuerra(),
MachadoTaurico(),
Mangual(),
Marreta(),
MarteloGuerra(),
Montante(),
Mosquete(),
Picareta(),
Pique(),
Pistola(),
Rede(),
Tacape(),
Tridente()]
