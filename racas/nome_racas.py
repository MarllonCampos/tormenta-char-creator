from enum import Enum
from racas import aggelus as aggelusClass
from racas import anao as anaoClass
from racas import dahllan as dahllanClass
from racas import elfo as elfoClass
from racas import goblin as goblinClass
from racas import golem as golemClass
from racas import humano as humanoClass
from racas import hynne as hynneClass
from racas import kliren as klirenClass
from racas import lefou as lefouClass
from racas import medusa as medusaClass
from racas import minotauro as minotauroClass
from racas import osteon as osteonClass
from racas import qareen as qareenClass
from racas import sereiatritao as sereiatritaoClass
from racas import silfide as silfideClass
from racas import sulfure as sulfureClass
from racas import trog as trogClass


class NomeRacas(Enum):
    aggelus = "Aggelus"
    anao = "Anao"
    dahllan = "Dahllan"
    elfo = "Elfo"
    goblin = "Goblin"
    golem = "Golem"
    humano = "Humano"
    hynne = "Hynne"
    kliren = "Kliren"
    lefou = "Lefou"
    medusa = "Medusa"
    minotauro = "Minotauro"
    osteon = "Osteon"
    qareen = "Qareen"
    sereiatritao = "SereiaTritao"
    silfide = "Silfide"
    sulfure = "Sulfure"
    trog = "Trog"

    @classmethod
    def race_class(cls, name):
        match name:
            case cls.aggelus.name:
                return aggelusClass.Aggelus()
            case cls.anao.name:
                return "anao"
            case cls.dahllan.name:
                return "dahllan"

            case cls.elfo.name:
                return "elfo"

            case cls.goblin.name:
                return "goblin"

            case cls.golem.name:
                return "golem"

            case cls.humano.name:
                return "humano"

            case cls.hynne.name:
                return "hynne"

            case cls.kliren.name:
                return "kliren"

            case cls.lefou.name:
                return "lefou"

            case cls.medusa.name:
                return "medusa"

            case cls.minotauro.name:
                return "minotauro"

            case cls.osteon.name:
                return "osteon"

            case cls.qareen.name:
                return "qareen"

            case cls.sereiatritao.name:
                return "sereiatritao"

            case cls.silfide.name:
                return "silfide"

            case cls.sulfure.name:
                return "sulfure"

            case cls.trog.name:
                return "trog"

            case _:
                print(f"NOT FOUND ERROR FOCKER,  {name}")
