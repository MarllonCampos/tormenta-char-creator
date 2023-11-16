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
                return anaoClass.Anao()
            case cls.dahllan.name:
                return dahllanClass.Dahllan()

            case cls.elfo.name:
                return elfoClass.Elfo()

            case cls.goblin.name:
                return goblinClass.Goblin()

            case cls.golem.name:
                return golemClass.Golem()

            case cls.humano.name:
                return humanoClass.Humano()

            case cls.hynne.name:
                return hynneClass.Hynne()

            case cls.kliren.name:
                return klirenClass.Kliren()

            case cls.lefou.name:
                return lefouClass.Lefou()

            case cls.medusa.name:
                return medusaClass.Medusa()

            case cls.minotauro.name:
                return minotauroClass.Minotauro()

            case cls.osteon.name:
                return osteonClass.Osteon()

            case cls.qareen.name:
                return qareenClass.Qareen()

            case cls.sereiatritao.name:
                return sereiatritaoClass.SereiaTritao()

            case cls.silfide.name:
                return silfideClass.Silfide()

            case cls.sulfure.name:
                return sulfureClass.Sulfure()

            case cls.trog.name:
                return trogClass.Trog()

            case _:
                print(f"NOT FOUND ERROR FOCKER,  {name}")
